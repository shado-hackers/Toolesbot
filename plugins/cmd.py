from pyrogram import *
import requests as re
from Config import *
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import wget
import os 

@app.on_message(filters.command('start'))
async def start_msg(client,message):
    await message.reply('**Hey '+message.from_user.first_name+"  🖐**\n\n__I'm TOOLS Bot, I can  DO many things build bu @shado_hackers")
    
@app.on_message(filters.command('help'))
async def help_msg(client,message):
    await message.reply(nothing more )
     
@app.on_message(filters.command('about'))
async def about_msg(client,message):
    await message.reply('__Developer : @shado_hackers (:\n\nSource Code : [GitHub Repo](https://github.com')
  
    
