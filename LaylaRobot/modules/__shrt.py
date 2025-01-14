# © zYxDevs at github.com/zYxDevs or t.me/Yoga_CIC

import aiohttp
from pyrogram import Client, filters

from LaylaRobot import pbot as yoga
from LaylaRobot import PDISK_KEY, dispatcher
from LaylaRobot.pyrogramee.errors import capture_err


@yoga.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
@capture_err
async def link_handler(_, message):
    link = message.matches[0].group(0)
    try:
        short_link = await pdisk_shortlink(link)
        await message.reply(f''' Click to Copy\n\n<code>{short_link}</code>.\n\nHere is your  [short link]({short_link})''', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def pdisk_shortlink(link):
    url = 'http://pdiskshortner.net/api'
    params = {'api': PDISK_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
