import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default



GENIUS_API = "RWmW7Y915_oCss4BglqUA6pU2B767XP6iBHdWsH4bGCHke1VbuZw1_BEdamn4kEC" # get it from https://genius.com/developers
LOG_GROUP = "-1001306080448" # Group ID for the log channel or leave it empty if not required 
BUG = "-1001306080448" #add your group id for getting error log messages or leave it empty if not required 

IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🎬 Title:</b> <a href={url}>{title}</a> [{year}] —<b>{kind}</b>\n\n<b>📆 Release:</b> <a href={url}/releaseinfo>{release_date}</a>\n<b>🌟 Rating:</b> <a href={url}/ratings>{rating} / 10</a>\n(based on <code>{votes}</code> user ratings.)\n\n<b>🎭 Genres:</b> #{genres}\n<b>📀 Runtime:</b> <code>{runtime} minutes</code>\n\n<b>☀️ Languages:</b> #{languages}\n<b>🌎 Country of Origin:</b> #{countries}\n<b>🎥 Director:</b> {director}\n\n<b><a href='https://t.me/omg_info'>© IMDb (Series & Movie) Studio</a></b>\n\n<b>✍️ Note:</b> <s>This message will be Auto-deleted after 10 hours to avoid copyright issues.</s>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
API_KEY='d79fe6458d9a29da04d15e3e' #if you have API replace this with your API KEY

base_url='https://v6.exchangerate-api.com/v6/'+API_KEY+'/latest/'
base_currency='INR' 

ibase_url='https://ifsc.razorpay.com/' 
head="**Detailed InFo**\n...................\n\n"
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
