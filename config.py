import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","20168427"))
API_HASH = getenv("API_HASH","fbb17a9011696e88f427f7608a855817")
BOT_TOKEN = getenv("BOT_TOKEN","5043078634:AAErKC_A1YrRYtOHcZ-NVX77DP04ipWlsYw")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://OPXVIRMUSIC:OPXVIRMUSIC@opxvirmusic.do072k5.mongodb.net/?retryWrites=true&w=majority")

LOGGER_ID = int(getenv("LOGGER_ID", "-1001672066567"))

GBAN_LOG_ID = int(getenv("GBAN_LOG", "-1001582846226"))

BOT_NAME = getenv("BOT_NAME", "[🇮🇳] Oᴘ✗Vɪʀ 🍂")
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "2116857965").split())
)
    
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/ROCKS_BOT_SUPPORT")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/Shayri_Music_Lovers")

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "900000")
)
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180000")
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/VIR99/iTzViR-MuSiC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN", "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")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "54000")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://te.legra.ph/file/fa898291a360b85acb1ab.mp4")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "ec8b977cffb74c2abc458c5e59724392")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "8d353de4053340359521957853ea2dcf")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "10")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)
TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "2073741824")
)


STRING1 = getenv("STRING_SESSION", "BQBzRNSx7pjViZ6MKhA1G7ocvpbj-mFkggR7o_jnDda5pUoyW6Bhc0umg7zBEPAKYehdPmEBjCH-YzIGfSfucsvOHJeIeBuK0KKwfkB2W12FkaUYoXBfsPRVSEE7GL6HpZKpQZg2DlkH1DNpLb5vSH1zkEl6HFlhAiajlH0iwvGjv_0Ac8svHfVVCjStxQgloXtuP_CQXyiAt7jdEfm1y1aPOx7hURF2bWAnyuxDPSJ0Tf3n2uuLqt1CH5S2qTLWkwOZTAtMPaiUDSr3GVP6pGOM130Nhsd5qGjUjRLSa5nB8LFWAiByvfld48-PcuJsa2wV5cEWKprOX4pDcP5OB3crAAAAATxbkKEA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Opxlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/fefb3d2468adb33461070.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/c384e0a5f8a49c1c331a3.png",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/075610fd1519afd9ed467.png"

GLOBAL_IMG_URL = "https://telegra.ph/file/d531b3f0827db188acc33.png"

STATS_IMG_URL = "https://telegra.ph/file/d531b3f0827db188acc33.png"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

STREAM_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

YOUTUBE_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
