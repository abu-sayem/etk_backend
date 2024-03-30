from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Production settings
DEBUG = True
# production.py
ALLOWED_HOSTS = ['localhost']


# Database (use production database settings)
# ...