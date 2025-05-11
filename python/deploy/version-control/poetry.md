# poetry

É um gerenciador de projetos e dependências para Python. 

## Instalação

> pipx install poetry

## Criando um projeto

> poetry new [projeto]

Ele criará uma estrutura de arquivos e pastas como essa:

```
.
├── [projeto]
│  └── __init__.py
├── pyproject.toml
├── README.md
└── tests
   └── __init__.py
```

O arquivo `pyproject.toml` foi criado para definir as especificações do projeto, alternativamente ao `requirements.txt`

## Criando ambiente virtual 

Permite instalar as bibliotecas necessárias dentro de um projeto criado com o `poetry`

> poetry install

Cria um arquivo `poetry.lock` com todas as versões das bibliotecas que serão utilizadas.

## Instalando bibliotecas no ambiente virtual

> poetry add [biblioteca]

## Ativando o ambiente virtual

> poetry shell

## Instalando bibliotecas em um grupo específico

Permite instalar bibliotecas que não serão utilizadas no ambiente de produção da aplicação, por exemplo. 

> poetry add --group [nome_grupo]

|a|a|
|a|a| 

**Obs.:** o comando `python í arquivo.py` permite rodar um arquivo no editor do terminal do Python.