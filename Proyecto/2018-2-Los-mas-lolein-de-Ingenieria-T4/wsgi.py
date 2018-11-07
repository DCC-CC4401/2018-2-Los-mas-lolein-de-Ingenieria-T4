"""
WSGI config for 2018-2-Los-mas-lolein-de-Ingenieria-T4 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "2018-2-Los-mas-lolein-de-Ingenieria-T4.settings")

application = get_wsgi_application()
