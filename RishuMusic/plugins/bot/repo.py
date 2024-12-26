from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ Ꝛᴀᴅʜᴇ ʀᴇᴘᴏs ⌾
 
◎ ʙʜᴀɢ ʙʜᴏsᴅɪᴋᴇ
 
◎ ʀᴇᴘᴏ ᴛᴏ ɴᴀ ᴅᴜɴɢᴀ
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴇʟᴘ •", url="https://t.me/ll_BOTCHAMBER_ll"),
          InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/ll_RADHE7_ll"),
          ],
               [
                InlineKeyboardButton("• ɴᴇᴛᴡᴏʀᴋ •", url=f"https://t.me/ll_BOTCHAMBER_ll"),
],
[
InlineKeyboardButton("• ᴏғғɪᴄɪᴀʟ ʙᴏᴛ •", url=f"https://t.me/RADHE_MUSIC_ROBOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/256b87e379dfd405b957d.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
