import os
class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5880758437:AAERYMlUmGifz6AQIdZkbiHuB6I6XzysR9c")

    API_ID = int(os.environ.get("API_ID", 2819362))

    API_HASH = os.environ.get("API_HASH", "578ce3d09fadd539544a327c45b55ee4")

    DATABASE = os.environ.get("DATABASE", "")

    DEV_NAME = os.environ.get("DEV_NAME", "Akhil")

    DEV_ID = set(int(x) for x in os.environ.get("DEV_ID", "1211202733").split())
