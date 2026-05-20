from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from app.core.config import APP_NAME, APP_VERSION
from app.repositories.import_batch_repository import ImportBatchRepository
from app.repositories.lead_repository import LeadRepository
from app.services.import_service import ImportService
from app.services.report_service import ReportService


class AppMenu:
    def __init__(
        self,
        import_service: ImportService,
        report_service: ReportService,
        lead_repository: LeadRepository,
        batch_repository: ImportBatchRepository,
    ) -> None:
        self.console = Console()
        self.import_service = import_service
        self.report_service = report_service
        self.lead_repository = lead_repository
        self.batch_repository = batch_repository

    def run(self) -> None:
        while True:
            self._show_header()
            self.console.print("[bold cyan]1[/] Importar planilha Excel")
            self.console.print("[bold cyan]2[/] Ver resumo dos dados")
            self.console.print("[bold cyan]3[/] Listar ultimos leads importados")
            self.console.print("[bold cyan]4[/] Ver historico de importacoes")
            self.console.print("[bold cyan]5[/] Exportar leads para CSV")
            self.console.print("[bold cyan]0[/] Sair")

            option = Prompt.ask("\nEscolha uma opcao", choices=["0", "1", "2", "3", "4", "5"])
            self.console.print()

            if option == "1":
                self._import_excel()
            elif option == "2":
                self._show_summary()
            elif option == "3":
                self._show_recent_leads()
            elif option == "4":
                self._show_import_history()
            elif option == "5":
                self._export_csv()
            elif option == "0":
                self.console.print("[green]Sistema finalizado com sucesso.[/]")
                break

            Prompt.ask("\nPressione Enter para continuar", default="")

    def _show_header(self) -> None:
        self.console.clear()
        self.console.print(
            Panel.fit(
                f"[bold white]{APP_NAME}[/]\n[cyan]Importador profissional de planilhas[/]\nVersao {APP_VERSION}",
                border_style="cyan",
            )
        )

    def _import_excel(self) -> None:
        file_path = Prompt.ask("Informe o caminho do arquivo .xlsx")
        try:
            result = self.import_service.import_file(file_path)
        except Exception as error:
            self.console.print(f"[bold red]Erro ao importar:[/] {error}")
            return

        self.console.print(f"[green]Arquivo importado:[/] {result.source_file}")
        self.console.print(f"Total de linhas: {result.total_rows}")
        self.console.print(f"Linhas validas: [green]{result.valid_rows}[/]")
        self.console.print(f"Linhas invalidas: [red]{result.invalid_rows}[/]")

        if result.errors:
            table = Table(title="Erros de validacao")
            table.add_column("Linha", justify="right")
            table.add_column("Problemas")
            for item in result.errors[:10]:
                table.add_row(str(item["linha"]), "; ".join(item["erros"]))
            self.console.print(table)

    def _show_summary(self) -> None:
        summary = self.lead_repository.get_summary()
        table = Table(title="Resumo Geral")
        table.add_column("Indicador")
        table.add_column("Valor", justify="right")
        table.add_row("Leads importados", str(summary["total_leads"]))
        table.add_row("Empresas distintas", str(summary["companies"]))
        table.add_row("Valor total", f"R$ {summary['total_value']:.2f}")
        table.add_row("Ticket medio", f"R$ {summary['average_value']:.2f}")
        self.console.print(table)

    def _show_recent_leads(self) -> None:
        rows = self.lead_repository.list_recent()
        table = Table(title="Ultimos Leads")
        for column in ["ID", "Nome", "Email", "Empresa", "Valor", "Arquivo"]:
            table.add_column(column)
        for row in rows:
            table.add_row(
                str(row["id"]),
                row["name"],
                row["email"],
                row["company"],
                f"R$ {row['value']:.2f}",
                row["source_file"],
            )
        self.console.print(table)

    def _show_import_history(self) -> None:
        rows = self.batch_repository.list_recent()
        table = Table(title="Historico de Importacoes")
        for column in ["ID", "Arquivo", "Total", "Validas", "Invalidas", "Data"]:
            table.add_column(column)
        for row in rows:
            table.add_row(
                str(row["id"]),
                row["source_file"],
                str(row["total_rows"]),
                str(row["valid_rows"]),
                str(row["invalid_rows"]),
                row["created_at"],
            )
        self.console.print(table)

    def _export_csv(self) -> None:
        output_path = self.report_service.export_recent_leads_csv()
        self.console.print(f"[green]Arquivo exportado com sucesso:[/] {output_path}")
