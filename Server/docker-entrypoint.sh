#!/bin/bash

sleep 4
cd Server
# python3 manage.py makemigrations graphs
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
echo "from django.contrib.auth.models import User; User.objects.create_superuser('client3', 'client3@example.com', 'AA-koala123456')" | python manage.py shell