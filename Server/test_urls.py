"""Unit testing for application urls.
"""
import os
import django
import sys
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib import admin

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AAB.settings')
django.setup()

#class TestUrls(SimpleTestCase):
#def test_admin_url_is_resolved(self):
# url = reverse(urls)
#print(resolve(url))




