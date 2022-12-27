import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "15523618"))
    API_HASH = os.environ.get("API_HASH", "8979514968543c31a37a3ed8a0726d83")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5861061051:AAEpaOoyoXIEKB7-Qy5uCSbETCsz52ZsFmI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIQBu7qvMo75ZwpI-9O25MJWS9sQlzja-MHFoLSqePFPXqFQrREm5VWJim8EXDozL9NL_5lnaYqc4W_8dt2edUbNwONGF1fIAhlrsP2INf9QXpHKiBVs2-w1_YsQKfYZLJb4LElQdqsdcq8ED-IjoPEjXvn6VMLqlkiYCepAkVXdWcjSyfdwzCVYou1b2eBmGR3gNANocceMx-l0X7Zp42H-k68UI5r81EOxMINGVzPtpC2m-nm7eMZSWbsWcpWpHGTPyEhgbsj5hHLQUDWUi_j0jwVcwsIMRLWJ4yes-NVLaIxnELgy-o_a6mmOI7NrJszJNqqNGNvmMS5cVmbb8-s89Mo=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "AnonMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "Hindi_English_Chatt")
    CHANNEL = os.environ.get("CHANNEL", "TheBotUpdate")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/535a7db55e251a316b807.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/5b5e408cfd6a6ee9e4bd7.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5119324429")) # required
