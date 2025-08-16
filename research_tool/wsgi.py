"""
WSGI config for research_tool project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'research_tool.settings')

application = get_wsgi_application()
