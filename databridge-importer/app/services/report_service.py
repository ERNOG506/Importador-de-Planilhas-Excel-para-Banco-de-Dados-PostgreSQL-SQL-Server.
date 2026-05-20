import csv
from datetime import datetime
from pathlib import Path

from app.core.config import EXPORTS_DIR
from app.repositories.lead_repository import LeadRepository


class ReportService:
    def __init__(self, lead_repository: LeadRepository) -> None:
        self.lead_repository = lead_repository

    def export_recent_leads_csv(self) -> Path:
        Path(EXPORTS_DIR).mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = Path(EXPORTS_DIR) / f"leads_exportados_{timestamp}.csv"
        rows = self.lead_repository.list_recent(limit=500)

        with output_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "name", "email", "phone", "company", "value", "source_file", "imported_at"],
            )
            writer.writeheader()
            writer.writerows(rows)

        return output_path
