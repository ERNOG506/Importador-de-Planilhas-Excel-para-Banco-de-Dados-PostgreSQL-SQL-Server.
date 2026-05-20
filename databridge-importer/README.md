# DataBridge Importer

Sistema profissional em Python para importar planilhas Excel, validar dados de clientes/leads e persistir as informacoes em banco SQLite.

Este projeto simula uma demanda comum em empresas: transformar planilhas recebidas de areas comerciais, financeiras ou administrativas em dados confiaveis dentro de um sistema.

## Objetivo do sistema

O DataBridge Importer permite que uma empresa importe uma planilha `.xlsx` com dados de clientes, valide cada linha, grave os registros corretos no banco de dados e gere relatorios para conferencia.

Ele foi criado para portfólio de quem busca estagio ou primeira vaga em TI, mostrando organizacao, boas praticas, banco de dados, validacoes e automacao de rotina administrativa.

## Funcionalidades

- Importacao de planilhas Excel `.xlsx`
- Validacao real de campos obrigatorios
- Persistencia em SQLite
- Historico de importacoes
- Resumo com indicadores de negocio
- Listagem dos ultimos registros importados
- Exportacao dos dados para CSV
- Interface de terminal com visual profissional
- Script para criar uma planilha de exemplo
- Testes automatizados para regras de validacao

## Tecnologias utilizadas

- Python 3.11+
- SQLite
- OpenPyXL
- Rich
- Pytest
- PowerShell
- Git e GitHub

## Estrutura de pastas

```text
databridge-importer/
├── app/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── ui/
│   └── main.py
├── data/
│   ├── exports/
│   └── imports/
├── docs/
├── scripts/
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## Arquitetura

O projeto usa separacao de responsabilidades:

- `models`: representa os dados principais do sistema.
- `database`: cria e gerencia conexao com o SQLite.
- `repositories`: concentram comandos de banco de dados.
- `services`: contem regras de negocio, leitura de Excel, validacao e relatorios.
- `ui`: contem o menu e a interacao com o usuario.
- `scripts`: automatizacoes auxiliares, como criacao da planilha de exemplo.
- `tests`: testes automatizados.

Essa organizacao facilita manutencao, testes e expansao futura para API, interface web ou banco PostgreSQL.

## Padrao esperado da planilha

A primeira linha da planilha deve ter exatamente estas colunas:

```text
nome | email | telefone | empresa | valor
```

Regras de validacao:

- Nome com pelo menos 3 caracteres
- Email em formato valido
- Telefone com pelo menos 10 digitos
- Empresa com pelo menos 2 caracteres
- Valor maior que zero

## Comandos PowerShell para criar e executar

Entre na pasta de projetos:

```powershell
cd "$env:USERPROFILE\Documents\Code\Projetos\databridge-importer"
```

Crie o ambiente virtual:

```powershell
py -3.14 -m venv .venv
```

Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependencias:

```powershell
.\.venv\Scripts\pip.exe install -r requirements.txt
```

Crie uma planilha de exemplo:

```powershell
.\.venv\Scripts\python.exe scripts\create_sample_excel.py
```

Execute o sistema:

```powershell
.\.venv\Scripts\python.exe -m app.main
```

Rode os testes:

```powershell
.\.venv\Scripts\pytest.exe
```

## Como usar

1. Execute o sistema.
2. Escolha a opcao `1 - Importar planilha Excel`.
3. Informe o caminho:

```text
data/imports/clientes_exemplo.xlsx
```

4. Veja o resumo da importacao.
5. Consulte os leads importados.
6. Exporte os dados para CSV se desejar.

## Codigo dos arquivos principais

O projeto esta organizado em arquivos pequenos e profissionais. Os principais sao:

- `app/main.py`: monta as dependencias e inicia o menu.
- `app/services/excel_reader.py`: le arquivos Excel e confere colunas obrigatorias.
- `app/services/validation_service.py`: aplica regras de negocio e validacao.
- `app/services/import_service.py`: coordena leitura, validacao e salvamento.
- `app/repositories/lead_repository.py`: salva e consulta leads no SQLite.
- `app/ui/menu.py`: apresenta a interface do usuario.

## Melhorias futuras

- Suporte a PostgreSQL e SQL Server
- Tela web com FastAPI ou Django
- Upload de arquivo pela interface web
- Autenticacao de usuarios
- Dashboard com graficos
- Logs profissionais em arquivo
- Exportacao para Excel formatado
- Integracao com CRM externo
- Validacao de duplicidade por email

## Funcionalidades que impressionam recrutadores

- Projeto resolve um problema real de empresas
- Usa banco de dados e camada de repositorio
- Tem validacoes reais e tratamento de erros
- Possui teste automatizado
- Usa ambiente virtual e dependencias organizadas
- Tem README completo
- Pode evoluir para ERP, CRM ou ferramenta administrativa

## Sugestoes de commits profissionais

```text
git add .
git commit -m "chore: create project structure"
git commit -m "feat: add excel import workflow"
git commit -m "feat: persist validated leads in sqlite"
git commit -m "feat: add terminal menu and reports"
git commit -m "test: add validation service tests"
git commit -m "docs: add complete project documentation"
```

## Organizacao de branches

Sugestao simples e profissional:

```text
main
feature/excel-import
feature/database-persistence
feature/reports
feature/tests
```

Fluxo recomendado:

```powershell
git checkout -b feature/excel-import
git add .
git commit -m "feat: add excel import workflow"
git checkout main
git merge feature/excel-import
```

## Como publicar no GitHub

```powershell
git init
git add .
git commit -m "feat: add databridge importer project"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/databridge-importer.git
git push -u origin main
```

No GitHub, adicione uma descricao como:

```text
Importador profissional de planilhas Excel com validacao, SQLite, relatorios e interface em Python.
```

## O que recrutadores analisam

- Clareza do README
- Organizacao de pastas
- Separacao entre interface, regra de negocio e banco
- Uso de Git com commits claros
- Projeto funcionando do inicio ao fim
- Tratamento de erros
- Capacidade de explicar as decisoes tecnicas
- Se o projeto parece resolver um problema real

## Por que este projeto e forte para portfólio

Ele demonstra que voce sabe construir uma solucao parecida com demandas reais de escritorio: importar planilhas, validar dados, salvar em banco e gerar relatorios. Isso conversa diretamente com vagas que pedem Excel, banco de dados, Python, ERP, CRM e rotinas administrativas.

## Nivel demonstrado

Este projeto demonstra nivel de programador junior inicial bem preparado: ainda simples o suficiente para explicar em entrevista, mas organizado com padroes que aparecem em sistemas profissionais.

## Habilidades tecnicas comprovadas

- Python com POO
- Manipulacao de Excel
- Banco de dados SQLite
- SQL basico
- Validacao de dados
- Arquitetura em camadas
- Interface de terminal
- Testes automatizados
- Git e GitHub
- Documentacao profissional

## Configuracao automatica opcional

Se preferir configurar tudo de uma vez, rode:

```powershell
.\scripts\setup.ps1
```

Esse script cria o ambiente virtual, instala as dependencias e gera a planilha de exemplo.
