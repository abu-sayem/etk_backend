from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from .base import *

# Local development settings
DEBUG = True
# dev.py
ALLOWED_HOSTS = ['localhost']


# Database (use local development database settings)
# ...