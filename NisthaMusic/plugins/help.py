from telethon import events, Button
from NisthaMusic import NisthaMusic, BOT_USERNAME
from Config import Config


btn =[
    [Button.inline("ᴀᴅᴍɪɴ", data="admin"), Button.inline("ʙᴀɴs", data="bans")],
    [Button.inline("ᴘɪɴs", data="pins"), Button.inline("ᴘᴜʀɢᴇs", data="purges")],
    [Button.inline("ᴘʟᴀʏ", data="play"), Button.inline("ᴢᴏᴍʙɪᴇs", data="zombies")],
    [Button.inline("ʟᴏᴄᴋs", data="locks"), Button.inline("ᴍɪsᴄ", data="misc")],
    [Button.inline("ʜᴏᴍᴇ", data="start")]]

HELP_TEXT = "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴇɴᴜ sᴇᴄᴛɪᴏɴ\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ"


@NisthaMusic.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_group:
       await event.reply("ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ɢᴇᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ʜᴇʟᴘ ᴍᴇɴᴜ", buttons=[
       [Button.url("ᴄʟɪᴄᴋ", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@NisthaMusic.on(events.NewMessage(pattern="^/start help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.reply(HELP_TEXT, buttons=btn)

@NisthaMusic.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.edit(HELP_TEXT, buttons=btn)
