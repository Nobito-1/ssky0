import asyncio

from Auput import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME, OWNER_USERNAME, SUPPORT_CHANNEL
from Auput.utils.bk import command

@app.on_message(filters.command("المطور", ["/", ".", "!",""]))
async def kontolmasukmemek(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/a2926dbe867154031b063.mp4",
        caption=f" ⌯  𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗦𝗢𝗨𝗥𝗖𝗘 𝙉𝙊𝘽𝙄𝙏𝙊  ⛧",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="لتنصيب بوت", url=f"https://t.me/{OWNER_USERNAME}"
            ),
            InlineKeyboardButton(
                text="𝙉𝙊𝘽𝙄𝙏𝙊 |⌯𖤒˼ ˹🖤˼", url=f"{SUPPORT_CHANNEL}"
            ),
        ],
                [
                    InlineKeyboardButton(
                        "ᴄʟᴏsᴇ", callback_data="close"
                    )
                ],
            ]
        )
    )
