#!/bin/bash
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate
# gunicorn oqtor.wsgi -b 0.0.0.0:8000
python3 manage.py runserver 0.0.0.0:8000
