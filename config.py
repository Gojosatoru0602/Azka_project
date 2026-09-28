import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "9999"))

DEVS = list(map(int, os.getenv("DEVS", "6385841558").split()))

API_ID = int(os.getenv("API_ID", "36584589"))

API_HASH = os.getenv("API_HASH", "9f3c2f0e976397151f9d4b46f5d45a45")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8598094418:AAH4dHdRFOHpTif4G5bsMnuKY")

OWNER_ID = int(os.getenv("OWNER_ID", "6385841558"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002886184276").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://rkhoirulbashar_db_user:CdHHAehaI7TWIQcm@cluster0.7bd6kkq.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002671518601"))