# This file serves as the WSGI entry point for Vercel.
# Placing it at the root ensures that Vercel sets the current working directory
# to the project root, keeping all module imports (like 'dashboard', 'accounts') fully functional.

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')

# Expose 'app' for Vercel's serverless environment
app = get_wsgi_application()
