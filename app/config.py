import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
VERSION = os.getenv("VERSION")
APP_SECRET = os.getenv("APP_SECRET")

def configure_app(app):
    app.config['ACCESS_TOKEN'] = ACCESS_TOKEN
    app.config['PHONE_NUMBER_ID'] = PHONE_NUMBER_ID
    app.config['VERIFY_TOKEN'] = VERIFY_TOKEN
    app.config['VERSION'] = VERSION
    app.config['APP_SECRET'] = APP_SECRET