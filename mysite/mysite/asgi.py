import os
import django
from channels.routing import get_default_application
# TODO: Could ASGI_APPLICATION difference cause issues?
# mysite.routing.application vs mysite.asgi:application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multichat.settings")
django.setup()
application = get_default_application()
