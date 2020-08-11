import os
from flask import Flask, request
import telegram
from bot_handler.config.credentials import BOT_TOKEN
from bot_handler.utils.setup_webhook import register_webhook
from bot_handler.config.db import Base, engine
app = Flask(__name__)

bot = telegram.Bot(token=BOT_TOKEN)


@app.before_first_request
def enable_webhook():
    Base.metadata.create_all(engine)
    if not register_webhook(bot):
        print("Error: Webhook not enabled")

@app.route("/")
def index():
    print("Hello World")

    if BOT_TOKEN != None:
        return {"message": "Bot token loaded successfully"}
    else:
        return {"error": "Something went wrong"}

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def bot_controller():
    # print(request.get_json(force=True))
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    print(f"Update: {update}")
    reply = f"Hey there, {update.message.chat.first_name}" if update.message.text == "/start" else "Noted"
    bot.sendMessage(
        chat_id=update.message.chat.id,
        text=reply,
        reply_to_message_id=update.message.message_id
        )
    return "OK"

if __name__ == "main":
    app.run(threaded=True, host="0.0.0.0", port=os.environ.get("PORT", 5000))