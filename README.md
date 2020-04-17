# Blog Python - Poetry  
  
API em Python para servir um site do tipo Blog.

O objetivo do projeto não é a API em si, mas os conceitos envolvidos em torno dela, como utilização do Poetry para gestão de dependências para desenvolvimento e produção.

Utilização da especificações contidas nas PEPs [517](https://www.python.org/dev/peps/pep-0517/) e [518](https://www.python.org/dev/peps/pep-0518/).

## O Projeto

O projeto é muito simples e consiste em basicamente 4 entidades: `Posts`, `Categories`, `Tags` e `UserRoles`. Todos os serviços necessários estão configurados no `docker-compose.yml`.

### Aplicação

Para iniciar a aplicação com as `migrations` e os `seeds`, basta executar o comando:
`docker-compose up app`

### Lint

As verificações de lint são realizadas pelo [PyLint](https://www.pylint.org/), [Flake8](https://flake8.pycqa.org/en/latest/), [pycodestyle](https://github.com/PyCQA/pycodestyle), [mypy](https://github.com/python/mypy), [black](https://github.com/psf/black) e [isort](https://github.com/timothycrosley/isort). Para iniciar as verificações basta executar o comando:
`docker-compose up lint`

### Testes

Os testes da aplicação são iniciados através do [tox](https://tox.readthedocs.io/en/latest/), que também pode ser iniciado com:
`docker-compose up integration-tests`

## O Poetry
  
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

## Ambientes Docker  

Quando o projeto é utilizado com Docker algumas coisas mudam no fluxo de trabalho.

A primeira mudança importante é que com Docker não existe mais a necessidade de um `virtualenv` para o projeto, afinal o container já é um ambiente isolado.

### Desenvolvimento 

No arquivo de definição `DockerfileDev` observe a instrução que configura o Poetry para não criar uma `virtualenv` automaticamente (esse é o comportamento padrão):

`poetry config virtualenvs.create false --local`

Um exemplo de arquivo de definição Docker para desenvolvimento se parece com o abaixo:

```Dockerfile
# DockerfileDev
FROM python:3.7.5-slim-stretch  
  
LABEL version="1.0.0"  
LABEL description="Blog API desenvolvido com Python, Django, Poetry e Docker"  
LABEL maintainer="Marcos V. Leal <marcosleal.prd@gmail.com>"  
LABEL environment="development"  
  
RUN pip install --upgrade pip  
RUN adduser --disabled-password --gecos '' worker  
  
USER worker  
  
WORKDIR /home/worker  
  
ENV PATH="/home/worker/.local/bin:${PATH}"  
  
COPY . /home/worker  
  
RUN pip install poetry  
RUN poetry config virtualenvs.create false --local  
RUN poetry install --no-root
```

Note que este arquivo implementa uma boa prática ao se trabalhar com containers, a não utilização do usuário `root`.

### Produção 

```Dockerfile
# Dockerfile
FROM python:3.7.5-slim-stretch  
  
LABEL version="1.0.0"  
LABEL description="Blog API desenvolvido com Python, Django, Poetry e Docker"  
LABEL maintainer="Marcos V. Leal <marcosleal.prd@gmail.com>"  
LABEL environment="production"  
  
RUN pip install --upgrade pip  
RUN adduser --disabled-password --gecos '' worker  
  
USER worker  
  
WORKDIR /home/worker  
  
ENV PATH="/home/worker/.local/bin:${PATH}"  
  
COPY . /home/worker  
  
RUN pip install poetry  
RUN poetry export -f requirements.txt -o requirements.txt  
RUN pip uninstall --yes poetry  
RUN pip install --require-hashes -r requirements.txt
```

O arquivo `Dockerfile` utilizado em produção é semelhante ao `DockerfileDev`, mas perceba as linhas:

```Dockerfile
RUN poetry export -f requirements.txt -o requirements.txt  
RUN pip uninstall --yes poetry  
RUN pip install --require-hashes -r requirements.txt
```

O Poetry é uma ferramenta promissora, mas na minha opinião não possui maturidade o suficiente para ser utilizada em produção, muito menos se estivermos falando de uma aplicação de microserviços.

Já o `pip`, padrão do Python para instalação de pacotes é bem confiável, além de ser muito mais rápido.

Entretanto, o Poetry nos permite gerar um `requirements.txt` a partir do `poetry.lock`, e com esse arquivo podemos utilizar o `pip` para instalar nossas dependências em produção de forma rápida e segura.

## Funcionalidades

Em Breve!