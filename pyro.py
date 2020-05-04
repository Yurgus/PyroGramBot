from pyrogram import Client
api_id = 1364592
api_hash = "bacb68050efb668d82dd9d1039759f49"

with Client("1298786254:AAEjXp5tUNmND7qSnMXvvnQICmXallRbloM", api_id, api_hash) as app:
    app.send_message("me", "Greetings from Pyrogram!")
    
app.run()
