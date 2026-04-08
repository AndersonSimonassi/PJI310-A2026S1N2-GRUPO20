"""
Configuração ASGI para o projeto SGO.

Expõe a aplicação ASGI no objeto ``application``.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sgo.settings')

application = get_asgi_application()
