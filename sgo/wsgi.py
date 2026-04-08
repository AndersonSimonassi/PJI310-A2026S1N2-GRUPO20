"""
Configuração WSGI para o projeto SGO.

Expõe a aplicação WSGI no objeto ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sgo.settings')

application = get_wsgi_application()
