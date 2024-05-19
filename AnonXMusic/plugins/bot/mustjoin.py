import random 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AnonXMusic import app

MISHI = [
    "https://telegra.ph/file/bedbb913da82612b429d7.jpg",
    "https://telegra.ph/file/584c89cf998bc64e94078.jpg",
    "https://telegra.ph/file/f3912e4e66b7a88721a0c.jpg",
    "https://telegra.ph/file/4d9ac2fbf4a74b25a46a5.jpg",
    "https://telegra.ph/file/1c6f431c58cc87e7e8bc3.jpg",
    "https://telegra.ph/file/a41d9e55d85be5e225921.jpg",
    "https://telegra.ph/file/4720efb6003b26d35de03.jpg",
    "https://telegra.ph/file/33460c709b084f4db6ec8.jpg"
    "https://telegra.ph/file/ac431378aba0501182934.jpg",
    "https://telegra.ph/file/972b3e5f2a860b3687e66.jpg",
]

#--------------------------

MUST_JOIN = "TeluguFriendsHub"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(random.choice(MISHI), caption=f"❅ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !\n\n❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ๛˹● 𝑻𝑶𝑴 ✘ 𝑱𝑬𝑹𝑹𝒀 𝑴𝑼𝑺𝑰𝑪 ●˼™ 🫧♡゙ ʙᴏᴛ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ʏᴏᴜ ᴊᴏɪɴᴇᴅ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("● ᴜᴘᴅᴀᴛᴇ ●", url="https://t.me/TitanNetwrk"),
                                InlineKeyboardButton("● sᴜᴘᴘᴏʀᴛ ●", url="https://t.me/TeluguFriendsHub"),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"● ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_ᴊᴏɪɴ ᴄʜᴀᴛ ●: {MUST_JOIN} !")