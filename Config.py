import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "15523618"))
    API_HASH = os.environ.get("API_HASH", "8979514968543c31a37a3ed8a0726d83")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5674233415:AAFFj3wdsnshrE_wri1hZqMbBxTuw2ctzeU")
    STRING_SESSION = os.environ.get("STRING_SESSION")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NisthaMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TeleBotsSupport")
    CHANNEL = os.environ.get("CHANNEL", "Fake_Peoples")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/535a7db55e251a316b807.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/5b5e408cfd6a6ee9e4bd7.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5881219743")) # required
