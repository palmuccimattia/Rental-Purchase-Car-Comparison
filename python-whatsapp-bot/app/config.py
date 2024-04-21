import sys
import os
from dotenv import load_dotenv
import logging
import json

def load_configurations(app):

    with open(os.getcwd() + "\\python-whatsapp-bot\\example.json", "r") as file:
        data = json.load(file)
    
    app.config["ACCESS_TOKEN"] = data["ACCESS_TOKEN"]
    app.config["YOUR_PHONE_NUMBER"] = data["YOUR_PHONE_NUMBER"]
    app.config["APP_ID"] = data["APP_ID"]
    app.config["APP_SECRET"] = data["APP_SECRET"]
    app.config["RECIPIENT_WAID"] = data["RECIPIENT_WAID"]
    app.config["VERSION"] = data["VERSION"]
    app.config["PHONE_NUMBER_ID"] = data["PHONE_NUMBER_ID"]
    app.config["VERIFY_TOKEN"] = data["VERIFY_TOKEN"]


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )