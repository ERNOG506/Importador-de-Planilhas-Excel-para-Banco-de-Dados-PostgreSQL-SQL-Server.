from pathlib import Path

from openpyxl import Workbook

output_dir = Path("data/imports")
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "clientes_exemplo.xlsx"

workbook = Workbook()
sheet = workbook.active
sheet.title = "Clientes"
sheet.append(["nome", "email", "telefone", "empresa", "valor"])
sheet.append(["Ana Costa", "ana.costa@empresa.com", "11987654321", "Costa Solucoes", 3500.75])
sheet.append(["Bruno Lima", "bruno.lima@mercado.com", "21999887766", "Mercado Lima", 1270.50])
sheet.append(["Caio Martins", "email-invalido", "123", "C", -10])
sheet.append(["Daniela Rocha", "daniela.rocha@tech.com", "31988776655", "Rocha Tech", 8450.00])

workbook.save(output_file)
print(f"Planilha de exemplo criada em: {output_file}")
