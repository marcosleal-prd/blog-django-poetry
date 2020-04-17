"""
WSGI config for blog_python project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
import os

from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application

from blog_python import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "propileu.settings")

if settings.USE_STATIC_FILE_HANDLER_FROM_WSGI:
    application = StaticFilesHandler(get_wsgi_application())
else:
    application = get_wsgi_application()
