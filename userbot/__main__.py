# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
""" Userbot start point """


import sys
from importlib import import_module
from platform import python_version

import requests
from pytgcalls import __version__ as pytgcalls
from pytgcalls import idle
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon import version


from userbot import BOT_TOKEN, BOT_USERNAME, BOT_VER, BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import DEVS, LOGS, blacklistayiin, bot, branch, call_py
from userbot.modules import ALL_MODULES
from userbot.utils import autobot, checking

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    name = user.first_name
    uid = user.id
    blacklistayiin = requests.get(
        "https://raw.githubusercontent.com/AyiinXd/Reforestation/master/ayiinblacklist.json"
    ).json()
    if user.id in blacklistayiin:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @mrismanaziz"
        )
        sys.exit(1)
    if 1878075436 not in DEVS:
        LOGS.warning(
            f"EOL\nArul-UserBot v{BOT_VER}, Copyright © 2021-2022 𝚖𝚞𝚑𝚊𝚍𝚊𝚖𝚙• <https://github.com/muhadamp>"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(f"Python Version - {python_version()}")
LOGS.info(f"Telethon Version - {version.__version__}")
LOGS.info(f"PyTgCalls Version - {pytgcalls.__version__}")

LOGS.info(
    f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
)

LOGS.info(
    f"✨ Arul-Userbot Version - {BOT_VER} [✧ 𝙰𝚁𝚄𝙻-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙳𝙸𝙰𝙺𝚃𝙸𝙵𝙺𝙰𝙽 ✧]")

LOGS.info(
    f"Jika {name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/wibu_telegram"
)


async def ayiin_userbot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"**✧ 𝙰𝚁𝚄𝙻-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**\n**✧ 𝙱𝙴𝚁𝙷𝙰𝚂𝙸𝙻 𝙳𝙸 𝙰𝙺𝚃𝙸𝙵𝙺𝙰𝙽 ✧**\n━━\n➠ **𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 -** `{BOT_VER}`\n➠ `@{branch}`\n➠ **𝙺𝙴𝚃𝙸𝙺** `{cmd}alive` **𝚄𝙽𝚃𝚄𝙺 𝙼𝙴𝙽𝙶𝙴𝙲𝙴𝙺 𝙱𝙾𝚃**\n━━\n➠ **𝙼𝙰𝙽𝙰𝙶𝙴𝙳 𝙱𝚈** : {name}",
            )

    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(JoinChannelRequest("@wibu_telegram"))
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass


bot.loop.run_until_complete(checking())
bot.loop.run_until_complete(ayiin_userbot_on())
if not BOT_TOKEN:
    bot.loop.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
