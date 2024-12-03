FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl && apt-get install -y libssl-dev
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH=/app/users_crm
RUN poetry --version

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root
COPY . /app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "users_crm.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
