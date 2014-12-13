# -*- coding: utf-8 -*-
from __future__ import absolute_import
__author__ = 'alex'
# http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html
import os
from celery import Celery
from django.conf import settings
# Configura los settings por default de Django para el programa "celery"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryTest.settings')
app = Celery('CeleryTest')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)