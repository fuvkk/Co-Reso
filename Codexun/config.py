## Disclaimer By Team Codexun

## Don't try to edit this file otherwise your bot will be crash.

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA8rSiB3u7elgAtwCGUWsu74xxsL_G2-aSEBe5rLCvxDNJUNRSubB9ZJwK3yczUDSHu_NkoAO751NaJaSTLN49XUe0Q-yNdtaqBOB-ZR3f9re_P5hDGULf41MtYWR2rygc9qcmdC-fRE5ZzFq2V6C_hgnNsh7CMoir1nCUyjm7C1VAQiCDfjbBTiPgy37MZDxkFLohLH74W-BQxDVgUVK_UCEisHCMx8oO2DrXkcVH3QJpoxVxitXTKTmpghvayYOmH_ecWfC2m9qLshg5bHekAYNL_lOestSrQVE6347doV2pXsUzYz_9x0tiRJNxKVa-grcDUvIrtzU3I3I1raPIXAAAAAWFUxV8A")
BOT_TOKEN = getenv("BOT_TOKEN", "5181191526:AAFJV8oyqjHW52trsQ2z01iORfDC782ohX0")
BOT_NAME = getenv("BOT_NAME", "Resso Music")
BOT_USERNAME = getenv("BOT_USERNAME", "Ressomusicbot")
ASSID = int(getenv("ASSID", "5927912799"))
ASSNAME = getenv("ASSNAME", "Resso Assistant")
ASSUSERNAME = getenv("ASSUSERNAME", "RessoNewVsn")
BOT_ID = int(getenv("BOT_ID", "5181191526"))
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/PavanMagar/CodexunMusicBot")
USERS = getenv("2056407064")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://codexun:TeamCodexun07@codexun.egmx5.mongodb.net/?retryWrites=true&w=majority")
API_ID = int(getenv("API_ID", "10098309"))
API_HASH = getenv("API_HASH", "aaacac243dddc9f0433c89cab8efe323")
OWNER_ID = int(getenv("OWNER_ID", "2056407064"))
UPDATE = getenv("UPDATE", "codexun")
SUPPORT = getenv("SUPPORT", "TeamCodexun")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/4d2838aac3120b0e04ce7.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/f2a2d31f60a9e0f3dbe94.png")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2056407064").split()))
ASSISTANT_NAME = getenv("ASSNAME")
COMMAND_PREFIXES = ("/ ! .").split()
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a085a3cea21f994264152.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
