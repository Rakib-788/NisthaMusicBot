import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "15523618"))
    API_HASH = os.environ.get("API_HASH", "8979514968543c31a37a3ed8a0726d83")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5674233415:AAFFj3wdsnshrE_wri1hZqMbBxTuw2ctzeU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzQBu6Nj9IOU1yUhVlgdlH_YPe4o_tnDhK7IRcuHNdLjhLwa0fX8O_CYt6-LiGjC2DdOyxcRqdbF80A2b9TNUlGOW2uwUDnT1F7aosmKcUMRbCgdnKU9pndZy-ZQxQEHCwg5OskPCVOtbgEFKvMnKyimO0lZQxQpVx4xZfHE3tbNhl1ttO1mUoGQlPb_4cBBEx-Kup3js5Jak1nyXbbrEhvMmzoxcKREOEnkKhgb5K8cVGk-yUZ2J4j4yjTce4Xw3u_XUv6spMgEq0k4pKYe3YH9SRmJEjRYwlrQAb68usI3DFXRqdYfPugbYDHUPFY07veMeNhO3A0VQgF4lrpoxTBrKrg=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NisthaMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "Hindi_English_Chatt")
    CHANNEL = os.environ.get("CHANNEL", "TheBotUpdate")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/535a7db55e251a316b807.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/5b5e408cfd6a6ee9e4bd7.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5945481632")) # required
