from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
🤗 Hello {}

I Am Telegram TOOLS Bot.

**__Send me a direct link and I will upload it to telegram as a file/video.__**

**Use Help Button To Know How To Use Me**
"""
    HELP_TEXT = """
𒊹︎︎︎ How To Upload File Or Media 

➪ Send Your Link For Upload File Or Media.

𒊹︎︎︎ How to set thumbnail

➪ Send Your Thumbnail Photo And Permanent Added Your Photo.

𒊹︎︎︎ How To Deleting Thumbnail

➪ Send /delthumb To Delete Your Thumbnail.

𒊹︎︎︎ How To Show Thumbnail 

➪ Send /showthumb To View Custom Thumbnail 
➪ How to use bot to avoid ban ❗❗ **[check out](https://telegra.ph/HOW-TO-AVOID-BAN-12-14)**
 
"""
    ABOUT_TEXT = """
**📛 My Name** : [Url xV2🚀](http://t.me/URLX_bot)

**❤️ Version** : [2 beta 🔥](http://t.me/URLX_bot)

**🤖 Source** : [Click](https://github.com)

**🧿 Language** : [Python 3.10.11](https://www.python.org/)

**📢 Framework** : [Pyrogram 1.4.16](https://docs.pyrogram.org/)

**👨‍💻 Developer** : [nothing](https://t.me/shado_hackers)

**IMPORTANT** [HOW TO USE](https://telegra.ph/HOW-TO-AVOID-BAN-12-14)

"""
 START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Settings', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about')
        ],[
        InlineKeyboardButton('Close', callback_data='close')
        ]]
 ) 
 

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Back', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about')
        ],[
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Back', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
