"""
WSGI config for miniblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

path = '\Django_Projects\miniblog\miniblog'
if path not in sys.path:
    sys.path.append(path)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniblog.settings')

os.environ['DJANGO_SETTINGS_MODULE'] = 'miniblog.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
