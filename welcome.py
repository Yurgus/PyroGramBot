from pyrogram import Client, Filters

app = Client("ServimSupport",1364592,"bacb68050efb668d82dd9d1039759f49")


@app.on_message(Filters.private)
def hello(client, message):
    message.reply_text("Hello {}".format(message.from_user.first_name))


app.run()
