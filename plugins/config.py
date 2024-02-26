import os
from os import environ
import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
        
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    API_ID = int(os.environ.get("API_ID", 12345))

    API_HASH = os.environ.get("API_HASH")

    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")

    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    LOGGER = logging

    #OWNER_ID = int(os.environ.get("OWNER_ID", ""))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "toolesbot")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    API_KEY='d79fe6458d9a29da04d15e3e' #if you have API replace this with your API KEY

    base_url='https://v6.exchangerate-api.com/v6/'+API_KEY+'/latest/'
    base_currency='INR'
    ADMINS = int(environ.get("ADMINS", ""))
    DB_URI = environ.get("DB_URI", "")
    DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
    OPENAI_API = environ.get("OPENAI_API", "")
    AI = is_enabled((environ.get("AI","True")), False)

