from telethon import events, Button, types
from NisthaMusic import NisthaMusic
from NisthaMusic.status import *
from Config import Config

PINS_TEXT = """
** ᴀʟʟ ᴛʜᴇ ᴘɪɴ ʀᴇʟᴀᴛᴇᴅ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ғᴏᴜɴᴅ ʜᴇʀᴇ; ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀᴛ ᴜᴘ ᴛᴏ ᴅᴀᴛᴇ ᴏɴ ᴛʜᴇ ʟᴀᴛᴇsᴛ ɴᴇᴡs ᴡɪᴛʜ ᴀ sɪᴍᴘʟᴇ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ.**

‣ `/pin` - ᴛᴏ ᴘɪɴɴᴇᴅ ᴀ ʀᴇᴘʟʏ ᴍsɢ.
‣ `/unpin` - ᴛᴏ ᴜɴᴘɪɴ ᴛʜᴇ ʟᴀᴛᴇsᴛ ᴘɪɴɴᴇᴅ ᴍsɢ.
‣ `/unpinall` - ᴛᴏ ᴜɴᴘɪɴᴀʟʟ ᴀʟʟ ᴘɪɴɴᴇᴅ ᴍsɢs ᴀᴛ ᴏɴᴄᴇ.
‣ `/pinned` - ᴛᴏ ɢᴇᴛ ᴄᴜʀʀᴇɴᴛ ᴘɪɴɴᴇᴅ ᴍsɢ.

**» ɴᴏᴛᴇ:** ᴀᴅᴅ `ɴᴏᴛɪғʏ` ᴀғᴛᴇʀ /ᴘɪɴ ᴛᴏ ɴᴏᴛɪғʏ ᴀʟʟ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀs.
"""

@NisthaMusic.on(events.NewMessage(pattern="^[?!/]pinned"))
async def get_pinned(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    chat_id = (str(event.chat_id)).replace("-100", "")

    Ok = await NisthaMusic.get_messages(event.chat_id, ids=types.InputMessagePinned()) 
    tem = f"The pinned message in {event.chat.title} is <a href=https://t.me/c/{chat_id}/{Ok.id}>here</a>."
    await event.reply(tem, parse_mode="html", link_preview=False)

@NisthaMusic.on(events.NewMessage(pattern="^[!?/]pin"))
@is_admin
async def pin(event, perm):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.pin_messages:
       await event.reply("ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs : ᴄᴀɴ ᴘɪɴ ᴍᴇssᴀɢᴇ.")
       return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍsɢ ᴛᴏ ᴘɪɴ ɪᴛ !")
       return
    input_str = event.pattern_match.group(1)
    if "notify" in input_str:
       await NisthaMusic.pin_message(event.chat_id, msg, notify=True)
       return
    await NisthaMusic.pin_message(event.chat_id, msg)   

@NisthaMusic.on(events.NewMessage(pattern="^[!?/]unpin"))
@is_admin
async def unpin(event, perm):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.pin_messages:
       await event.reply("ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs : ᴄᴀɴ ᴘɪɴ ᴍᴇssᴀɢᴇ.")
       return
    chat_id = (str(event.chat_id)).replace("-100", "")
    ok = await NisthaMusic.get_messages(event.chat_id, ids=types.InputMessagePinned())
    await Stark.unpin_message(event.chat_id, ok)
    await event.reply(f"Successfully unpinned [this](t.me/{event.chat.username}/{ok.id}) message.", link_preview=False)

@NisthaMusic.on(events.NewMessage(pattern="^[!?/]permapin"))
@is_admin
async def permapin(event, perm):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.pin_messages:
       await event.reply("ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs : ᴄᴀɴ ᴘɪɴ ᴍᴇssᴀɢᴇ.")
       return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍsɢ ᴛᴏ ᴘᴇʀᴍᴀᴘɪɴ ɪᴛ.")
       return
    hn = await NisthaMusic.send_message(event.chat_id, msg.message)
    await NisthaMusic.pin_message(event.chat_id, hn, notify=True)


@NisthaMusic.on(events.NewMessage(pattern="^[!?/]unpinall"))
async def unpinall(event, perm):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.pin_messages:
       await event.reply("ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs : ᴄᴀɴ ᴘɪɴ ᴍᴇssᴀɢᴇ.")
       return
    UNPINALL = """
ᴀʀᴇ ʏᴏᴜ sᴜʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ
ᴜɴᴘɪɴ ᴀʟʟ ᴍsɢs
ᴛʜɪs ᴀᴄᴛɪᴏɴ ᴄᴀɴ'ᴛ ʙᴇ ᴜɴᴅᴏɴᴇ !
"""

    await NisthaMusic.send_message(event.chat_id, UNPINALL, buttons=[
    [Button.inline("ᴄᴏɴғɪʀᴍ", data="unpin")], 
    [Button.inline("ᴄᴀɴᴄᴇʟ", data="cancel")]])

@NisthaMusic.on(events.callbackquery.CallbackQuery(data="unpin"))
async def confirm(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await NisthaMusic.unpin_message(event.chat_id)
        await event.edit("ᴜɴᴘɪɴɴᴇᴅ ᴀʟʟ ᴍsɢs !")
        return 

    await event.answer("ɢʀᴏᴜᴘ ᴄʀᴇᴀᴛᴏʀ ʀᴇǫᴜɪʀᴇᴅ !")

@NisthaMusic.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await event.edit("ᴜɴᴘɪɴɴɪɴɢ ᴏғ ᴀʟʟ ᴍsɢs ʜᴀs ʙᴇᴇɴ ᴄᴀɴᴄᴇʟʟᴇᴅ !")
        return 

    await event.answer("ɢʀᴏᴜᴘ ᴄʀᴇᴀᴛᴏʀ ʀᴇǫᴜɪʀᴇᴅ !")


@NisthaMusic.on(events.callbackquery.CallbackQuery(data="pins"))
async def _(event):

    await event.edit(PINS_TEXT, buttons=[[Button.inline("ʙᴀᴄᴋ", data="help")]])
