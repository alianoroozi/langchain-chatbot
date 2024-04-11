FROM python:3.11-slim

RUN pip install poetry

RUN poetry config virtualenvs.create false

WORKDIR /code

COPY ./pyproject.toml ./README.md ./poetry.lock* ./

COPY ./package[s] ./packages

COPY ./app ./app

RUN poetry install  --no-root

EXPOSE 8080

CMD exec uvicorn app.server:app --host 0.0.0.0 --port 8080
