#!/usr/bin/env bash
set -e

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python -m venv /code/venv_lin

/bin/bash -c "source /code/venv_lin/bin/activate"

python -m pip install --upgrade pip
python -m pip install -I -r requirements.txt

echo "Migrating..."
./manage.py makemigrations
./manage.py migrate

echo "-------------------------------------"
echo "#  Creating user with:              #"
echo "#       username: admin             #"
echo "#       password: pass              #"
echo "-------------------------------------"
echo "
from django.contrib.auth.models import User
try:
       profile = User.objects.create_superuser('admin', 'admin@example.com', 'pass')
except:
    pass
" | python manage.py shell

exec "$@"