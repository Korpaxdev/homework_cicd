FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction

COPY . .