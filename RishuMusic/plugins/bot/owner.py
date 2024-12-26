from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - ʀᴀᴅʜᴇ sᴀɴᴀᴛᴀɴɪ
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - ᴘʀɪɴᴄᴇ ᴘᴀᴛᴇʟ
│├─────────────────╯
├┼─────────────────⦿
├┤~ @ll_RADHE7_ll
├┤~ @ll_BOTCHAMBER_ll
├┤~ @DP_WORLD7
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @ll_RADHE7_ll
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 ", url=f"https://t.me/ll_RADHE7_ll")
        ],
        [
          InlineKeyboardButton("𝗗𝗣 𝗖𝗢𝗟𝗟𝗘𝗖𝗧𝗜𝗢𝗡", url="https://t.me/DP_WORLD7"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://t.me/ll_BOTCHAMBER_ll"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/ll_BOTCHAMBER_ll"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/ll_RADHE_MUSIC_ROBOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/94f5088fdc7a0450bfa0a.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
