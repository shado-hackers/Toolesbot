from pyrogram import *
import requests as re
from Config import *
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import wget
import os 

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    if not update.from_user:
        return await update.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, update)
    await bot.send_message(
     #   Config.LOG_CHANNEL,
        #   f"NEW_USER: \n\nNew User [{update.from_user.first_name}](tg://user?id={update.from_user.id}) started @{Config.BOT_USERNAME} !!"
    )
    
    #if Config.UPDATES_CHANNEL:
    #  fsub = await handle_force_subscribe(Client, update)
   #   if fsub == 400:
  #      return
    await update.reply_text(
        text=Translation.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS
    )
