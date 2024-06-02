import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from Auput import app
from Auput.utils.vip_ban import admin_filter

SPAM_CHATS = {}


@app.on_message(
    filters.command(["utag", "uall",], prefixes=["/", "@", ".", "#",""]) & admin_filter
)
async def tag_all_users(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if len(message.text.split()) == 1:
        await message.reply_text(
            "** اضف الكلام مع تاك, مثال »** `تاك اشتقت لك`"
        )
        return

    text = message.text.split(None, 1)[1]
    if text:
        await message.reply_text(
            "**تاك [تاك مستمر] تم بنجاح!**\n\n**๏ تاك كُل سبع ثواني.**\n\n**➥ يمكنك ايقاق التاك بواسطة » `تعطيل تاك`**"
        )

    SPAM_CHATS[chat_id] = True
    f = True
    while f:
        if SPAM_CHATS.get(chat_id) == False:
            await message.reply_text("**تم ايقاف التاك بنجاح.**")
            break
        usernum = 0
        usertxt = ""
        try:
            async for m in app.get_chat_members(message.chat.id):
                if m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                if usernum == 1:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}")
                    usernum = 0
                    usertxt = ""
                    await asyncio.sleep(7)
        except Exception as e:
            print(e)


@app.on_message(
    filters.command(
        ["stoputag", "stopuall", "offutag", "offuall", "utagoff", "ualloff"],
        prefixes=["/", ".", "@", "#",""],
    )
    & admin_filter
)
async def stop_tagging(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if SPAM_CHATS.get(chat_id) == True:
        SPAM_CHATS[chat_id] = False
        return await message.reply_text("**الرجاء الانتضار لأيقاف التاك ...**")
    else:
        await message.reply_text("**التاك متوقف الآن **")