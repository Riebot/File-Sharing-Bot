#(©)ZauteKm

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>▷ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n▷ Language : <code>Python3</code>\n▷ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n▷ Movies/Series : <a href='https://t.me/joinchat/prE6ALN6x2hkY2E1'>Join now</a>\n▷ Channel : <a href='https://t.me/mizotginfotel'>Mizo Infotel Channel</a>\n▷ Support Group : <a href='https://t.me/mizotelegram'>Join now</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Search", switch_inline_query_current_chat = ''),
                        InlineKeyboardButton(" Go Inline", switch_inline_query = '')
                    ],
                    [
                        InlineKeyboardButton("Close 🔐", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text = f"<b>Min hmandân túr tlângpui:</b>\n\n1.1. Inline Mode hmangin i Series/Movies duh i Search thei.\n2. He <a href='https://t.me/joinchat/prE6ALN6x2hkY2E1'>Group</a> hi Join-in i Series duh hming thupui lo thawn tawp la, i hmu nghâl ang.\n\n<b>How to Get Files:</b> <a href='https://t.me/mizotginfotel/37'>Press me 🥰</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Search", switch_inline_query_current_chat = ''),
                        InlineKeyboardButton(" Go Inline", switch_inline_query = '')
                    ],
                    [
                        InlineKeyboardButton("Close 🔐", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
