# Guia rapido para entrevista

## Pitch de 30 segundos

Desenvolvi um importador de planilhas Excel em Python para simular uma rotina real de empresas. O sistema valida dados de clientes, grava registros corretos em SQLite, registra historico de importacoes e permite exportar relatorios. Organizei o projeto em camadas para facilitar manutencao e expansao.

## Decisoes tecnicas

- SQLite foi escolhido por ser simples de executar localmente e demonstrar persistencia real.
- Repositories isolam o acesso ao banco.
- Services concentram regras de negocio.
- Rich melhora a experiencia da interface sem criar complexidade de frontend.
- Pytest cobre validacoes principais.

## Como explicar uma melhoria futura

Eu evoluiria este projeto para uma API com FastAPI, conectaria em PostgreSQL e adicionaria uma tela web para upload da planilha e acompanhamento das importacoes.
