FROM python:3.12-slim

# 1. Системные зависимости
RUN apt-get update && apt-get install -y postgresql-client curl gnupg gettext && rm -rf /var/lib/apt/lists/*

# 2. Poetry
RUN pip install --no-cache-dir poetry

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 3. Установка Python-зависимостей
COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi

# 4. Node.js + npm
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get update && apt-get install -y nodejs

# 5. Копировать весь проект
COPY . .

# 6. Tailwind build
# RUN npm install && npm run build

# 7. Entrypoint
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
