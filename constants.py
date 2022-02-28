import os
from dotenv import load_dotenv
load_dotenv()

class Constants:
    PORT = os.environ.get('PORT')
    DATABASE_URL = os.environ.get('DATABASE_URL')