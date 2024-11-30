FROM python:3.12-slim

# Встановлюємо залежності для Poetry
RUN apt-get update && apt-get install -y curl && apt-get install -y libssl-dev

# Встановлюємо Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Додаємо Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH=/app/src
# Перевіряємо, що Poetry встановлений
RUN poetry --version

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли проекту, в тому числі pyproject.toml та poetry.lock
COPY pyproject.toml poetry.lock /app/

# Встановлюємо залежності через Poetry
RUN poetry install --no-root

# Копіюємо весь код в контейнер
COPY . /app

# Відкриваємо порт для додатка
EXPOSE 8000

# Команда для запуску FastAPI з uvicorn
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
