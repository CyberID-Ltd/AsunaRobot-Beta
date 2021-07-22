from os import environ
import aiohttp
from pyrogram import Client, filters

from LaylaRobot import pbot as yoga
from LaylaRobot import PDISK_KEY, BITLY_KEY, dispatcher
from LaylaRobot.pyrogramee.errors import capture_err


@yoga.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
@capture_err
async def link_handler(_, message):
    link = message.matches[0].group(0)
    try:
        short_link = await pdisk_shortlink(link)
        await message.reply(f''' Click to Copy - <code>{short_link}</code>.\nHere is your  [short link]({short_link})''', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def pdisk_shortlink(link):
    url = 'http://pdiskshortner.net/api'
    params = {'api': PDISK_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

__mod_name__ = "Shortlink"
__help__ = """
*Pdisk shortener*
 ❍ /pdisk `<your link>` *:* shorten your url using pdisk shortener.
 ❍ /bitly `<your link>` *:* shorten your url using bitly shortener (no ads).
*Note*
This module is not complete yet, maybe have a bug.

*Don't delete this if you appreciate my work.*
© @Yoga_CIC *&* @SpreadNetworks
"""

