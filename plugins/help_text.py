#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
# the Strings used for this "thing"
from translation import Translation

from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as Clinton
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

START_BTNS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                'Update Channel', url='https://t.me/myownbots'),
            InlineKeyboardButton(
                'Support Chat', url='https://telegram.me/DevsChats')
        ]
    ]
)

HELP_BTNS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="➰️ Channel", url=f"https://telegram.me/MYOWNBOTS"),
            InlineKeyboardButton(text="👥️️ Support", url=f"https://telegram.me/DEVSCHATS"),
          ],[
             InlineKeyboardButton(text="Documentation 📃", url=f"https://graph.org/How-to-Use-URL-Uploader-Bot-03-02"),
        ]
    ]
)

ABOUT_BTNS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                '⚙️ Support', url='https://telegram.me/DevsChats'),
            InlineKeyboardButton(
                '➰️ Channel', url='https://telegram.dog/myownbots')
        ]
    ]
)

@Clinton.on_message(filters.regex(pattern=".*http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/).*"))
async def yturl(bot, update):
  await bot.send_message(
    chat_id=update.chat.id,
    text=f"Please Use @YouTubeDownloader_XBot for Download YouTube Content",
    disable_web_page_preview=True,
    reply_to_message_id=update.message_id
  )

@Clinton.on_message(filters.private & filters.command(["about"]))
async def about_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=ABOUT_BTNS,
        reply_to_message_id=update.message_id
    )

@Clinton.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=HELP_BTNS,
        reply_to_message_id=update.message_id
    )


@Clinton.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=START_BTNS,
        reply_to_message_id=update.message_id
    )
