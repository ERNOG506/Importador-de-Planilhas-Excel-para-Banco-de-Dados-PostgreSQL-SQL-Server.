from app.core.paths import ensure_project_directories
from app.database.connection import DatabaseConnection
from app.repositories.import_batch_repository import ImportBatchRepository
from app.repositories.lead_repository import LeadRepository
from app.services.excel_reader import ExcelReader
from app.services.import_service import ImportService
from app.services.report_service import ReportService
from app.services.validation_service import LeadValidationService
from app.ui.menu import AppMenu


def build_menu() -> AppMenu:
    ensure_project_directories()
    database = DatabaseConnection()
    database.initialize()

    lead_repository = LeadRepository(database)
    batch_repository = ImportBatchRepository(database)
    import_service = ImportService(
        excel_reader=ExcelReader(),
        validator=LeadValidationService(),
        lead_repository=lead_repository,
        batch_repository=batch_repository,
    )
    report_service = ReportService(lead_repository)

    return AppMenu(import_service, report_service, lead_repository, batch_repository)


def main() -> None:
    menu = build_menu()
    menu.run()


if __name__ == "__main__":
    main()
