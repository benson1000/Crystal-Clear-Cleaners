#!/bin/sh

set -e

# Wait for the database to be ready
/wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is ready!"
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi