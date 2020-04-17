#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py seedsuperuser
python manage.py seed
python manage.py drf_create_token admin
python manage.py runserver ${BIND_ADDRESS}:${BIND_PORT}
