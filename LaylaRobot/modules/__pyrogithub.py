# © @Mr_Dark_Prince & @zYxDevs
import aiohttp
from pyrogram import filters
from LaylaRobot import pbot
from LaylaRobot.pyrogramee.errors import capture_err


__mod_name__ = "Github"
__help__ = """
● /github `<github username>` - Returns info about a GitHub user or organization.

● /repo `<github username>` - Return the GitHub user or organization repository list (Limited at 40)
"""


@pbot.on_message(filters.command('github'))
@capture_err
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/github username")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                updated_at = result['updated_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                public_repos = result['public_repos']
                public_gists = result['public_gists']
                followers = result['followers']
                following = result['following']
                id = result['id']
                type = result['type']
                hireable = result['hireable']
                email = result['email']
                caption = f"""**Info Of {name}**
**👨‍💼 Username:** `{username}`
**🔖 Account ID:** `{id}`
**📝 Account type:** `{type}`
**📶 Profile Link:** [Click Here]({url})
**📨 Email:** `{email}`
**✍️ Bio:** `{bio}`
**🏢 Company:** `{company}`
**🌚 Hireable:** `{hireable}`
**⛵️ Public Repos:** `{public_repos}`
**🚁 Public Gists:** `{public_gists}`
**📍 Location:** `{location}`
**➡️ Followers:** `{followers}`
**⬅️ Following:** `{following}`
**📒 Created at:** `{created_at}`
**♻️ Updated at:** `{updated_at}`
**🌍 Website:** `{blog}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)
