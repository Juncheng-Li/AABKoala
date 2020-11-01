#!/bin/bash

sh -c "/wait-for-it.sh -t 0 db:3306 --strict -- echo \"MySQL is up\""
python3 manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('client', 'client@example.com', 'AA-koala123456')" | python manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'root@example.com', 'AA-koala123456')" | python manage.py shell
python3 manage.py runserver 0.0.0.0:8000