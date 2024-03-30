import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

if os.environ.get('ENVIRONMENT') == 'local':
    from .settings.local import *
elif os.environ.get('ENVIRONMENT') == 'dev':
    from .settings.dev import *
elif os.environ.get('ENVIRONMENT') == 'production':
    from .settings.production import *

DEBUG = True
ALLOWED_HOSTS = ['localhost']
