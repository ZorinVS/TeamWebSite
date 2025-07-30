#!/bin/sh

# Подождать, пока база будет доступна
echo "⏳ Ожидание PostgreSQL..."
until pg_isready -h db -p 5432 > /dev/null 2>&1; do
  sleep 1
done
echo "✅ PostgreSQL готов."

echo "📦 Выполняем миграции..."
python manage.py makemigrations
python manage.py migrate

echo "🎯 Собираем статику..."
python manage.py collectstatic --noinput

echo "🔑 Создаем суперпользователя..."
python create_superuser.py

echo "📝 Загружаем посты..."
python manage.py load_posts

echo "🚀 Запускаем Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000

