import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6027500067:AAG-veKTUgl3nSIT2rpiK_FMAWv_60vPDqg")

    API_ID = int(os.environ.get("API_ID", "4546803"))

    API_HASH = os.environ.get("API_HASH", "08ad181fba3b05e1141db96175cab60e")
    
    API_KEY = os.environ.get("API_KEY", "847yfgv1x2aurspiqj3")

    # AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())

    # PRIVATE = bool(os.environ.get("PRIVATE", ""))

    
