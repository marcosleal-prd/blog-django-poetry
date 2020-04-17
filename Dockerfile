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
