from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
🤗 Hello {}

I Am Telegram TOOLS Bot.

**__Send me a direct link and I will upload it to telegram as a file/video.__**

**Use Help Button To Know How To Use Me**
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
    
