from pyrogram import Client
import re
import asyncio
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()
import config
from dotenv import load_dotenv
from ..logging import LOGGER
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")



assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="Auput1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="Auput2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="Auput3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="Auput4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="Auput5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("KKC8C")
                await self.one.join_chat("KKC8C")
                await self.one.join_chat("KKC8C")
                await self.one.join_chat("KKC8C")
                
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOG_GROUP_ID, "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ !")  
                
            except:
                LOGGER(__name__).error(
                    "Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.me.first_name}")
        
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("iqsupp")
                await self.two.join_chat("mgimt")
                await self.two.join_chat("ehs4ss")
                await self.two.join_chat("xv7amo")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOG_GROUP_ID, "Assistant Started")
                
            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.me.first_name}")
       
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("iqsupp")
                await self.three.join_chat("xv7amo")
                await self.three.join_chat("mgimt")
                await self.three.join_chat("ehs4ss")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(
                f"Assistant Three Started as {self.three.me.first_name}"
            )

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("xv7amo")
                await self.four.join_chat("mgimt")
                await self.four.join_chat("ehs4ss")
                await self.four.join_chat("iqsupp")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(
                f"Assistant Four Started as {self.four.me.first_name}"
            )

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("xv7amo")
                await self.five.join_chat("mgimt")
                await self.five.join_chat("ehs4ss")
                await self.five.join_chat("iqsupp")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOG_GROUP_ID, "Assistant 5 started !")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(
                f"Assistant Five Started as {self.five.me.first_name}"
            )

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
