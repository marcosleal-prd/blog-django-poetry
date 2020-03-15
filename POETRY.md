# Blog Python - Poetry

API em Python para um Blog, ou seja, este é um CMS.

## Requisitos

### Poetry

O Poetry é o mais novo *queridinho* da comunidade com a proposta de simplificar o processo de gestão de dependências.

#### Arquivos

Substitui os arquivos abaixo por apenas um chamado `pyproject.toml`.

- `setup.py`
- `requirements.txt`
- `manifest.in`
- `Pipfile`

#### Comandos

Substitui a necessidade de utilizar os comandos abaixo por apenas `poetry`.

- `build`
- `sdist`
- `twine`
- `pip`
- `hashes`
- `pip-tools`

#### Mais

- Respeita a arvore do gestor de versão
- Força o uso [SEMVER](https://semver.org/)
- Sistema de resolução de conflitos mais robusto
- Inspirado no Cargo (Rust) e Composer (PHP)

> Python packaging and dependency management made easy

Para saber mais [visite o site oficial](https://python-poetry.org/)

**Nesse momento o Poetry só é recomendado para o ambiente de desenvolvimento.**

## Ambientes

### Desenvolvimento

#### 1. `poetry new <nome_do_projeto>` e `pyproject.toml`

Para criar um novo projeto com Poetry basta executar o comando `poetry new meuprojeto` e já vamos ter o `pyproject.toml` (este formato não é do Poetry, é oficial do Python) no e toda a estrutura base do projeto.

```
# pyproject.toml
[tool.poetry.dependecies]
python="~2.7 || ^3.2"
dynaconf="^2.0"
```
#### 2. Comando `poetry env use <python_version>`

Este comando cria uma virtualenv para ser utilizada no projeto. O mais legal disso é que podemos criar mais de uma virtualenv para o mesmo projeto.

#### 3. Comando `poetry shell`

Uma vez criada a virtualenv, este comando realiza a ativação.

#### 4. Comando `poetry install`

Gera o arquivo `Poetry.lock` para gerir os hashes das dependências.

#### 5. Comando `poetry export`

Gera o arquivo `requirements.txt` com todos hashes necessários para o funcionado da aplicação.

#### 6. Comando `poetry build`

Gera o build da aplicação, um arquivo chamado `project.whl`.

### Produção

#### Gerar arquivo `requirements.txt`

```bash
poetry export -f requirements.txt -o requirements.txt
```

#### Instalação
```bash
pip install --require-hashes -r requirements.txt
```
