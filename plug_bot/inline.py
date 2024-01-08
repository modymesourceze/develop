from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio


@bot.on_inline_query(filters.regex("^الاوامر$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("⓵",callback_data="help1"),
             InlineKeyboardButton("⓶",callback_data="help2"),
             InlineKeyboardButton("⓷",callback_data="help3"),
             ],
             [
             InlineKeyboardButton("⓸",callback_data="help4"),
             InlineKeyboardButton("⓹",callback_data="help5"),
             InlineKeyboardButton("⓺",callback_data="help6"),
             ],
             [
             InlineKeyboardButton("⓻",callback_data="help7"),
             InlineKeyboardButton("⓼",callback_data="help8"),
             InlineKeyboardButton("⓽",callback_data="help9"),
             InlineKeyboardButton("❁",callback_data="help10"),
             ],
             [
             InlineKeyboardButton("↯ - قناه السورس - ↯",url="https://t.me/Source_Ze"),
             ],
             [
             InlineKeyboardButton("♆ - جروب المساعدة - ♆",url="https://t.me/ZeSupport"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="اوامر البوت",
                input_message_content=InputTextMessageContent(
                    "• ⟣=====⧼[᥉᥆υᖇᥴᥱ ɀᥱ](https://t.me/Source_Ze)⧽=====⟢\n• ⓵ اوامر الخاص\n• ⓶ اوامر القنوات والمجموعات \n• ⓷ اوامر اليوتيوب \n• ⓸ اوامر الاذاعه\n• ⓹ اوامر الرفع \n• ⓺ اوامر النسب\n• ⓻ اوامر اضافية \n• ⓼ اوامر تسلية1 \n• ⓽ اوامر تسلية2 \n• ❁ اوامر الزخرفة \n• ⟣=====⧼ [᥉᥆υᖇᥴᥱ ɀᥱ](https://t.me/Source_Ze)⧽=====⟢"
                ),
                url="https://t.me/Source_Ze",
                description="᥉᥆υᖇᥴᥱ ɀᥱ",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )
