"""
Django configuration file for unit testing docker containers.
"""

from settings import *
import os

ALLOWED_HOSTS = ['*']
DEBUG = True

ENV = 'development'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': 'flowchat_db',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_database'
        }
    }
}
