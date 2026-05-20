from app.database.connection import DatabaseConnection


class ImportBatchRepository:
    def __init__(self, database: DatabaseConnection) -> None:
        self.database = database

    def save(self, source_file: str, total_rows: int, valid_rows: int, invalid_rows: int) -> None:
        with self.database.connect() as connection:
            connection.execute(
                """
                INSERT INTO import_batches (source_file, total_rows, valid_rows, invalid_rows)
                VALUES (?, ?, ?, ?)
                """,
                (source_file, total_rows, valid_rows, invalid_rows),
            )

    def list_recent(self, limit: int = 10) -> list[dict]:
        with self.database.connect() as connection:
            rows = connection.execute(
                """
                SELECT id, source_file, total_rows, valid_rows, invalid_rows, created_at
                FROM import_batches
                ORDER BY created_at DESC, id DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
            return [dict(row) for row in rows]
