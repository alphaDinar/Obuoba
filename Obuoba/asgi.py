import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Obuoba.settings')

django_asgi_app = get_asgi_application()

import notify.routing

application = ProtocolTypeRouter(
    {
        "http" : django_asgi_app,
        "websocket" : AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(notify.routing.websocket_urlpatterns))
        )
    }
)
