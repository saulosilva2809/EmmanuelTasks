#!/bin/sh
set -e

echo "⏳ Esperando serviços..."
sleep 5

echo "🧠 Rodando migrations..."
python manage.py migrate --noinput

exec "$@"