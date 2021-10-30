import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
ARQ_API_KEY = getenv("ARQ_API_KEY")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Veez Music")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/8628c642a266a22effd8c.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/0f6f8a8a5ad69fe5ecf3d.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/5dd3d6d64ccd785ae5af2.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/84f09e57f97f6e1bb3cba.jpg")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/84f09e57f97f6e1bb3cba.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/5dd3d6d64ccd785ae5af2.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "Eagle_Xrobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "EagleAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Mutualan_Cari_Teman")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "infobotrelax")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "Manusiabajingann")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "ᴇᴀɢʟᴇ")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://t.me/ikichannellll"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
