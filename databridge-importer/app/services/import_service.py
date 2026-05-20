from dataclasses import dataclass
from pathlib import Path

from app.repositories.import_batch_repository import ImportBatchRepository
from app.repositories.lead_repository import LeadRepository
from app.services.excel_reader import ExcelReader
from app.services.validation_service import LeadValidationService


@dataclass(frozen=True)
class ImportResult:
    source_file: str
    total_rows: int
    valid_rows: int
    invalid_rows: int
    errors: list[dict]


class ImportService:
    def __init__(
        self,
        excel_reader: ExcelReader,
        validator: LeadValidationService,
        lead_repository: LeadRepository,
        batch_repository: ImportBatchRepository,
    ) -> None:
        self.excel_reader = excel_reader
        self.validator = validator
        self.lead_repository = lead_repository
        self.batch_repository = batch_repository

    def import_file(self, file_path: str) -> ImportResult:
        records = self.excel_reader.read(file_path)
        valid_leads = []
        errors = []

        for record in records:
            lead, record_errors = self.validator.validate(record)
            if lead:
                valid_leads.append(lead)
            else:
                errors.append({"linha": record.get("linha"), "erros": record_errors})

        source_file = Path(file_path).name
        if valid_leads:
            self.lead_repository.save_many(valid_leads, source_file)

        result = ImportResult(
            source_file=source_file,
            total_rows=len(records),
            valid_rows=len(valid_leads),
            invalid_rows=len(errors),
            errors=errors,
        )
        self.batch_repository.save(source_file, result.total_rows, result.valid_rows, result.invalid_rows)
        return result
