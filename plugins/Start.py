import os
import time
import psutil
import shutil
import string
import asyncio
from pyrogram import Client, filters
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from plugins.config import Config
from plugins.translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
      await update.reply_text(
        text=Translation.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
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
