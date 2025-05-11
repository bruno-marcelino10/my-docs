# ruff

Ferramenta escrita em Rust que serve como Linter (análise estática) e Formatter (padronização do código)

As ferramentas utilizadas são:

* I (Isort): Checagem de ordenação de imports em ordem alfabética
* F (Pyflakes): Procura por alguns erros em relação a boas práticas de código
* E (Erros pycodestyle): Erros de estilo de código
* W (Avisos pycodestyle): Avisos de coisas não recomendadas no estilo de código
* PL (Pylint): Como o F, também procura por erros em relação a boas práticas de código
* PT (flake8-pytest): Checagem de boas práticas do Pytest

## Comandos importantes

> ruff check --diff 

Mostra o que precisa ser alterado no código para que as boas práticas sejam seguidas

> ruff check .

Mostra os códigos de infrações de boas práticas

> ruff check . --fix

Faz algumas correções de boas práticas automaticamente

> ruff format .

Executa a formatação do código em relação as convenções de estilo de código