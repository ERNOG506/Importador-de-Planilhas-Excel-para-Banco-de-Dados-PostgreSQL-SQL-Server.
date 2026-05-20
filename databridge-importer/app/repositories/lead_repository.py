from app.database.connection import DatabaseConnection
from app.models.customer_lead import CustomerLead


class LeadRepository:
    def __init__(self, database: DatabaseConnection) -> None:
        self.database = database

    def save_many(self, leads: list[CustomerLead], source_file: str) -> None:
        with self.database.connect() as connection:
            connection.executemany(
                """
                INSERT INTO customer_leads (name, email, phone, company, value, source_file)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        lead.name,
                        lead.email,
                        lead.phone,
                        lead.company,
                        float(lead.value),
                        source_file,
                    )
                    for lead in leads
                ],
            )

    def list_recent(self, limit: int = 20) -> list[dict]:
        with self.database.connect() as connection:
            rows = connection.execute(
                """
                SELECT id, name, email, phone, company, value, source_file, imported_at
                FROM customer_leads
                ORDER BY imported_at DESC, id DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
            return [dict(row) for row in rows]

    def get_summary(self) -> dict:
        with self.database.connect() as connection:
            row = connection.execute(
                """
                SELECT
                    COUNT(*) AS total_leads,
                    COALESCE(SUM(value), 0) AS total_value,
                    COALESCE(AVG(value), 0) AS average_value,
                    COUNT(DISTINCT company) AS companies
                FROM customer_leads
                """
            ).fetchone()
            return dict(row)
