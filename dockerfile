FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl build-essential && \
    apt-get clean

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

RUN poetry install

# CMD ["poetry", "run", "python", "src/main.py"]