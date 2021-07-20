from LaylaRobot.events import register
from LaylaRobot import OWNER_ID
from LaylaRobot import telethn as tbot
import os 
from PIL import Image, ImageDraw, ImageFont
import shutil 
import random, re
import glob
import time
from telethon.tl.types import InputMessagesFilterPhotos


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/b3da75d390da29a9c5145.jpg", 
                         "https://telegra.ph/file/005b97f50828f37a047da.jpg", 
                         "https://telegra.ph/file/b72f6bac98d44c351bd2b.jpg", 
                         "https://telegra.ph/file/9839fafe31b53c5062939.jpg",
                         "https://telegra.ph/file/fd89b1da833a2b0acb556.jpg",
                         "https://telegra.ph/file/ffb3135a7f2487a3d3a51.jpg", 
                         "https://telegra.ph/file/f94bda5ac2351a4886184.jpg", 
                         "https://telegra.ph/file/1edeb3a44dfba865a82b4.jpg",
                         "https://telegra.ph/file/09c60e5bf55185bb0135a.jpg", 
                         "https://telegra.ph/file/5319696d88ba2ee93242d.jpg", 
                         "https://telegra.ph/file/eddf990a5a00f92057060.jpg", 
                         "https://telegra.ph/file/947d50055ceadc13dc102.jpg",
                         "https://telegra.ph/file/73db070410bfbf383cdaf.jpg", 
                         "https://telegra.ph/file/e29ae5b20db5260a8572c.jpg", 
                         "https://telegra.ph/file/3dca3ed4cfcb42cedbdb0.jpg", 
                         "https://telegra.ph/file/81a7bbfba66534d53ea4b.jpg",
                         "https://telegra.ph/file/2db2995ccd40ae845c23a.jpg",
                         "https://telegra.ph/file/97f9ef8ae71d547e49846.jpg", 
                         "https://telegra.ph/file/1aceaa7b12127b382f284.jpg", 
                         "https://telegra.ph/file/880c9d272bbf00936b910.jpg",
                         "https://telegra.ph/file/a7ba13dc7ac5560319836.jpg",
                         "https://telegra.ph/file/576866d045642e2cd7bac.jpg", 
                         "https://telegra.ph/file/20f957ca20bc072fd82b8.jpg", 
                         "https://telegra.ph/file/7a214f9ed5ece48eace4b.jpg",
                         "https://telegra.ph/file/e5a7021e047cf15e5302e.jpg", 
                         "https://telegra.ph/file/a690626d02f52158764a7.jpg", 
                         "https://telegra.ph/file/cf8a76fa9ea38f2b78fb1.jpg", 
                         "https://telegra.ph/file/768d3c1ffcf5b9e2b4dba.jpg",
                         "https://telegra.ph/file/b0c438928bbc72e8e3a50.jpg", 
                         "https://telegra.ph/file/2baa9963ddb5ae6fedeb4.jpg", 
                         "https://telegra.ph/file/e551de18484171033c3a4.jpg", 
                         "https://telegra.ph/file/113610ce3b4f729ac242c.jpg",
                         "https://telegra.ph/file/671f017f22167720c6f5a.jpg",
                         "https://telegra.ph/file/2805b3f1bd4e8425caae2.jpg", 
                         "https://telegra.ph/file/3e554a3123dacf2127e8f.jpg", 
                         "https://telegra.ph/file/4cbce5c3047dfaa9c9c45.jpg",
                         "https://telegra.ph/file/4cfee7f9d0521c5f7d4f6.jpg",
                         "https://telegra.ph/file/7074a8277f3bdd1b3c1eb.jpg", 
                         "https://telegra.ph/file/be0d7dec5378220d17a8c.jpg", 
                         "https://telegra.ph/file/06712323005d2f880b4b9.jpg",
                         "https://telegra.ph/file/455f306254085436664e2.jpg", 
                         "https://telegra.ph/file/fd84d9c7af6504cc5aa47.jpg", 
                         "https://telegra.ph/file/086f63db36d046ab6fc93.jpg", 
                         "https://telegra.ph/file/769118c95233de797eedf.jpg",
                         "https://telegra.ph/file/9daab97cf09f811d3afb2.jpg", 
                         "https://telegra.ph/file/a9a6d728539db7809372a.jpg", 
                         "https://telegra.ph/file/c538b6d3ec43c2060484c.jpg", 
                         "https://telegra.ph/file/3dfcf7e53681a09477909.jpg",
                         "https://telegra.ph/file/f9beeb561e04117a8d9f2.jpg",
                         "https://telegra.ph/file/70ec8a88ec40d9abe88c2.jpg", 
                         "https://telegra.ph/file/f90c247920415c68eb13f.jpg", 
                         "https://telegra.ph/file/c46eb2f6b5899822176db.jpg",
                         "https://telegra.ph/file/5d9841569011d2b02c6d8.jpg", 
                         "https://telegra.ph/file/49dfa36966b1f616f5a23.jpg",
                         "https://telegra.ph/file/83bf06b24d34d6485b4a0.jpg", 
                         "https://telegra.ph/file/755e43ca2a136add7e97a.jpg",
                         "https://telegra.ph/file/48768282a87b99a762b7b.jpg", 
                         "https://telegra.ph/file/82bfc4d06e41af55ef3af.jpg",
                         "https://telegra.ph/file/112285f42925daaa1d88a.jpg", 
                         "https://telegra.ph/file/8d53a8377141fdc2560c2.jpg",
                         "https://telegra.ph/file/8e9f0829dcaf5fdcda37b.jpg", 
                         "https://telegra.ph/file/013acc3f41364cc2197b9.jpg",
                         "https://telegra.ph/file/f4f23a6cbd3311592884a.jpg", 
                         "https://telegra.ph/file/9d306403b4479402a817c.jpg",
                         "https://telegra.ph/file/8b591e59f3078ee3b380d.jpg", 
                         "https://telegra.ph/file/5e69c2de9de20add17131.jpg",
                         "https://telegra.ph/file/13ec29c885445f5f19f3c.jpg", 
                         "https://telegra.ph/file/296693a68d8c36fbe70ca.jpg",
                         "https://telegra.ph/file/42cb3f4c8f92e81680edc.jpg", 
                         "https://telegra.ph/file/80ff2d48906c112f0b98b.jpg",
                         "https://telegra.ph/file/4cd1e55373ac3bbe05643.jpg", 
                         "https://telegra.ph/file/e55c44659aa67d9c9251e.jpg",
                         "https://telegra.ph/file/93d48cfd34544c3b0ceb9.jpg", 
                         "https://telegra.ph/file/238168426aa20c5de5497.jpg",
                         "https://telegra.ph/file/f9649cf1465e6be4fd53e.jpg", 
                         "https://telegra.ph/file/1ea4870a7b1d3840b309b.jpg",
                         "https://telegra.ph/file/b0ba28648a0303d57a4ad.jpg", 
                         "https://telegra.ph/file/b989e19ae42fd0fe304e6.jpg",
                         "https://telegra.ph/file/61467f319e19bde90d6e7.jpg", 
                         "https://telegra.ph/file/be39245f7de2d7c638968.jpg"
                         ]

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./LaylaRobot/resources/blackbg.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./LaylaRobot/resources/Chopsic.otf", 330)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "LogoByAsuna.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @YogaWaifuBot\nSupport @YBotsSupport")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @YBotsSupport, {e}')



   
@register(pattern="^/wlogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./LaylaRobot/resources/blackbg.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    font = ImageFont.truetype("./LaylaRobot/resources/Maghrib.ttf", 1000)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white")
    fname2 = "LogoByAsuna.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @YogaWaifubot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @YBotsSupport, {e}')

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__help__ = """
 ❍ /logo text :  Create your logo with your name
 ❍ /wlogo text :  Create your logo with your name

 """
__mod_name__ = "Logo"
