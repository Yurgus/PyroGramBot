from pyrogram import Client

api_id = 1364592
api_hash = "bacb68050efb668d82dd9d1039759f49"

with Client("Universal_shat_bot", api_id, api_hash) as app:
    app.send_message("me", "Greetings from **Pyrogram**!")
