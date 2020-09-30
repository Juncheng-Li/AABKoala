#!/bin/bash

sleep 7
cd Server
python3 manage.py makemigrations graphs
python3 manage.py migrate graphs
python3 manage.py runserver 0.0.0.0:8000