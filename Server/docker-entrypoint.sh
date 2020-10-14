#!/bin/bash

# sleep 20
./wait-for-it.sh db:3306 -- echo "MySQL is up"
# python3 manage.py makemigrations graphs
python3 manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('client', 'client@example.com', 'AA-koala123456')" | python manage.py shell
python3 manage.py runserver 0.0.0.0:8000