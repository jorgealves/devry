FROM python:3.9-alpine

WORKDIR /workspace

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1

RUN apk add --no-cache bash curl gcc git groff libffi-dev musl-dev openssh-client && \
    /usr/local/bin/python -m pip install --upgrade pip && \
    pip --no-cache-dir install poetry=="$POETRY_VERSION"

WORKDIR /workspace

COPY README.md .
COPY pyproject.toml .
COPY poetry.lock .
COPY src ./src

RUN poetry config virtualenvs.create false && \
    poetry install 
