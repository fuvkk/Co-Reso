## Disclaimer By Team Codexun

## Don't try to edit this file otherwise your bot will be crash.

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBNI-P2ele45XAoq25aRLNOEc5jyHA__tmJ2dyVSnotOfhvAYrdgAI_g-1KAFrMT9Ng7edhk1taSk55CMZYlkiubKW0D3LjQb1Rs5Y2H2h4CnFtbZdg3MVWFEtIbIAJZjsmNI_TZUgOV5-_EK3Zh5t1mKmXF6CxNYc-R4pceGPFDDOQuRlrzM_TJIRN5TVhhDozRGei-PFd_xFafKvs4o3NKkNHDQ_EDaShN-pnd7Ar7mac6h48gj7Ry9lFM07eJL1bA8zIz7pb2b_pFB-MpVrEGybmk_heQkr-SkTlJDa1heKWG765dKGonvc9jeMayASJMj8kWACrX6JkshfjIrnJAAAAAUQujzgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5181191526:AAHQE0indJGdrFooBVWRXgSOoJjluwG0J9A")
BOT_NAME = getenv("BOT_NAME", "Resso Music")
BOT_USERNAME = getenv("BOT_USERNAME", "Ressomusicbot")
ASSID = int(getenv("ASSID", "5438869304"))
ASSNAME = getenv("ASSNAME", "Resso Assistant")
ASSUSERNAME = getenv("ASSUSERNAME", "RessoMusicA")
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
