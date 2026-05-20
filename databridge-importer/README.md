# DataBridge Importer

Importador de planilhas Excel desenvolvido em Python para validação e persistência de dados em banco SQLite.

O projeto foi criado para automatizar um fluxo comum em ambientes corporativos: receber dados em planilhas, validar informações e armazenar registros de forma estruturada.

---

## Funcionalidades

* Importação de arquivos `.xlsx`
* Validação automática de dados
* Persistência em SQLite
* Histórico de importações
* Exportação de registros para CSV
* Relatórios resumidos
* Interface de terminal
* Testes automatizados

---

## Tecnologias utilizadas

* Python 3.11+
* SQLite
* OpenPyXL
* Rich
* Pytest
* Git/GitHub

---

## Estrutura do projeto

```text id="4f8mvt"
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
├── requirements.txt
└── README.md
```

---

## Arquitetura

O projeto foi organizado em camadas para facilitar manutenção e expansão:

* `models` → entidades principais
* `database` → conexão e gerenciamento do banco
* `repositories` → operações SQL
* `services` → regras de negócio e validações
* `ui` → interface do terminal
* `tests` → testes automatizados

---

## Formato esperado da planilha

```text id="tqjlwm"
nome | email | telefone | empresa | valor
```

### Regras de validação

* Nome mínimo de 3 caracteres
* Email válido
* Telefone com pelo menos 10 dígitos
* Empresa obrigatória
* Valor maior que zero

---

## Execução do projeto

### Clonar o repositório

```powershell id="m2xw6j"
git clone https://github.com/SEU-USUARIO/databridge-importer.git
cd databridge-importer
```

### Criar ambiente virtual

```powershell id="3drn0d"
py -3.14 -m venv .venv
```

### Ativar ambiente virtual

```powershell id="sq53bi"
.\.venv\Scripts\Activate.ps1
```

### Instalar dependências

```powershell id="j6pfd8"
pip install -r requirements.txt
```

### Gerar planilha de exemplo

```powershell id="jlwmpt"
python scripts/create_sample_excel.py
```

### Executar aplicação

```powershell id="1q7e5o"
python -m app.main
```

### Executar testes

```powershell id="6g7n7j"
pytest
```

---

## Funcionalidades futuras

* Integração com PostgreSQL
* API REST com FastAPI
* Dashboard web
* Sistema de autenticação
* Logs estruturados
* Upload de arquivos pela interface

---

## Git e versionamento

### Exemplo de commits

```text id="xgnx9j"
feat: add excel import workflow
feat: persist leads in sqlite
feat: add export to csv
test: add validation tests
docs: improve readme
```

### Organização de branches

```text id="sy6x6o"
main
feature/excel-import
feature/database
feature/reports
feature/tests
```

---

## Objetivos do projeto

* Trabalhar com manipulação de planilhas Excel
* Aplicar validação de dados
* Utilizar persistência com SQLite
* Organizar uma aplicação Python em camadas
* Implementar testes automatizados
* Simular um fluxo comum de sistemas administrativos

---

## Habilidades utilizadas

* Python
* SQL
* Manipulação de arquivos Excel
* Arquitetura em camadas
* Tratamento de erros
* Testes automatizados
* Git e GitHub
* Organização de projetos backend
