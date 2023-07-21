#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $DB_HOST 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

exec "$@"