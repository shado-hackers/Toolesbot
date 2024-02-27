import os
import time
import psutil
import shutil
import string
import asyncio
from pyrogram import Client, filters
from asyncio import TimeoutError
from plugins.config import *
from plugins.database import db
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from plugins.config import Config
from plugins.translation import Translation
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)
LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""
@Client.on_message(filters.command(["start"]))
async def start_message(c,m):
    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(Config.LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo(f"https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg",
        caption="**ʜɪ** 👋\n\n**ɪ ᴀᴍ ᴀ 𝚃𝚘𝚘𝚕𝚜 𝚋𝚘𝚝 𝙸 𝚌𝚊𝚗 𝚍𝚘 𝚖𝚊𝚗𝚢 𝚝𝚑𝚒𝚗𝚐𝚜 𝚌𝚑𝚎𝚌𝚔 /𝚑𝚎𝚕𝚙 𝚖𝚎𝚗𝚞**\n\n⭕ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[OMG INFO](https://t.me/OMG_INFO)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('💝 sᴜʙsᴄʀɪʙᴇ 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 ᴄʜᴀɴɴᴇʟ', url='https://t.me/OMG_INFO')
                    ],  
                    [
                        InlineKeyboardButton("❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url='https://t.me/shado_hackers'),
                        InlineKeyboardButton("🤖 ᴜᴘᴅᴀᴛᴇ", url='https://t.me/OMG_INFO')
                    ]
                ]
            )
        )
  
@Client.on_message(filters.command(["help"]))
async def help(bot, update):
      await update.reply_text(
        text=Translation.HELP_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
      )
@Client.on_message(filters.command(["about"]))
async def about(bot, update):
      await update.reply_text(
        text=Translation.ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
     )  
