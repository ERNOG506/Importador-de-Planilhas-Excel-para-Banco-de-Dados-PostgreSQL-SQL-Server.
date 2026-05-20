# DataBridge Importer

Sistema profissional desenvolvido em Python para importação, validação e persistência de dados de clientes/leads a partir de planilhas Excel.

O projeto simula uma necessidade real encontrada em empresas comerciais, financeiras e administrativas: transformar planilhas desorganizadas em dados confiáveis dentro de um sistema estruturado.

---

# Visão Geral

O **DataBridge Importer** automatiza o processo de:

* leitura de arquivos Excel `.xlsx`;
* validação de dados;
* tratamento de inconsistências;
* persistência em banco SQLite;
* geração de relatórios;
* exportação de registros.

O sistema foi projetado com arquitetura organizada, separação de responsabilidades e foco em boas práticas de desenvolvimento backend.

---

# Demonstração das funcionalidades

## Principais recursos

* Importação de planilhas Excel
* Validação automática de dados
* Persistência em banco SQLite
* Histórico de importações
* Exportação para CSV
* Relatórios resumidos
* Interface de terminal profissional
* Testes automatizados
* Arquitetura escalável
* Estrutura semelhante a sistemas corporativos reais

---

# Tecnologias utilizadas

| Tecnologia   | Finalidade                 |
| ------------ | -------------------------- |
| Python 3.11+ | Backend principal          |
| SQLite       | Persistência de dados      |
| OpenPyXL     | Leitura de planilhas Excel |
| Rich         | Interface terminal moderna |
| Pytest       | Testes automatizados       |
| Git/GitHub   | Versionamento              |
| PowerShell   | Automação do ambiente      |

---

# Arquitetura do projeto

O projeto foi estruturado utilizando separação em camadas para facilitar manutenção, escalabilidade e organização.

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

## Responsabilidades das camadas

| Camada       | Responsabilidade                 |
| ------------ | -------------------------------- |
| models       | Representação das entidades      |
| database     | Conexão e inicialização do banco |
| repositories | Operações SQL                    |
| services     | Regras de negócio                |
| ui           | Interface do usuário             |
| tests        | Testes automatizados             |
| scripts      | Automação auxiliar               |

---

# Problema de negócio resolvido

Empresas frequentemente recebem dados em planilhas Excel contendo:

* informações inconsistentes;
* dados incompletos;
* duplicidades;
* erros de preenchimento.

O DataBridge Importer automatiza a validação e padronização desses dados antes do armazenamento.

Isso reduz:

* retrabalho;
* erros humanos;
* inconsistências em CRM/ERP;
* tempo operacional.

---

# Regras de validação

O sistema realiza validações reais de negócio:

* Nome mínimo de 3 caracteres
* Email válido
* Telefone com pelo menos 10 dígitos
* Empresa obrigatória
* Valor acima de zero

Formato esperado da planilha:

```text
nome | email | telefone | empresa | valor
```

---

# Execução do projeto

## Clonar o repositório

```powershell
git clone https://github.com/SEU-USUARIO/databridge-importer.git
cd databridge-importer
```

## Criar ambiente virtual

```powershell
py -3.14 -m venv .venv
```

## Ativar ambiente

```powershell
.\.venv\Scripts\Activate.ps1
```

## Instalar dependências

```powershell
pip install -r requirements.txt
```

## Gerar planilha de exemplo

```powershell
python scripts/create_sample_excel.py
```

## Executar sistema

```powershell
python -m app.main
```

## Executar testes

```powershell
pytest
```

---

# Funcionalidades que demonstram maturidade técnica

Este projeto demonstra:

* arquitetura em camadas;
* separação de responsabilidades;
* persistência de dados;
* validação robusta;
* uso de ambiente virtual;
* organização profissional;
* testes automatizados;
* versionamento com Git;
* documentação técnica.

---

# Diferenciais do projeto

## Simulação de cenário corporativo real

O projeto foi pensado para simular demandas comuns em:

* ERP
* CRM
* sistemas administrativos
* automação empresarial
* backoffice

---

## Estrutura pronta para evolução

O sistema pode evoluir facilmente para:

* API REST com FastAPI
* dashboard web
* autenticação de usuários
* PostgreSQL
* integração com sistemas externos
* upload via navegador
* deploy em nuvem

---

# Testes automatizados

O projeto utiliza `Pytest` para validação das regras de negócio críticas.

Exemplos:

* validação de email;
* validação de telefone;
* campos obrigatórios;
* valores inválidos.

---

# Git e versionamento

Exemplo de commits utilizados:

```text
feat: add excel import workflow
feat: persist validated leads in sqlite
feat: add terminal dashboard
test: add validation service tests
docs: improve project documentation
```

Branches sugeridas:

```text
main
feature/excel-import
feature/database
feature/reports
feature/tests
```

---

# O que este projeto demonstra para recrutadores

## Hard Skills

* Python
* SQLite
* Manipulação de Excel
* SQL
* Validação de dados
* Arquitetura backend
* Testes automatizados
* Git/GitHub

## Soft Skills percebidas

* Organização
* Capacidade analítica
* Estruturação de projeto
* Atenção a detalhes
* Pensamento voltado para negócio

---

# Nível técnico demonstrado

O projeto demonstra perfil de:

* Desenvolvedor Python Júnior
* Estagiário acima da média
* Backend iniciante com boas práticas

Apesar de ser um projeto de portfólio, sua estrutura se aproxima da organização encontrada em aplicações reais.

---

# Melhorias futuras

* PostgreSQL
* Docker
* API REST
* Interface web
* Login/autenticação
* Dashboard analítico
* Logs estruturados
* Deploy em cloud
* Integração com CRM

---

# Autor

Desenvolvido por um estudante apaixonado por tecnologia, automação e desenvolvimento de software, com foco em evolução contínua e construção de projetos práticos para o mercado de TI.
