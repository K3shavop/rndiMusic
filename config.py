from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/e51b7c6580e8e7aea55e8.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/e51b7c6580e8e7aea55e8.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/indiaxchats")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_Keshav_op")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6179690246").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
