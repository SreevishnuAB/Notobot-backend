import os
from flask import Flask, request
import telegram
from bot_handler.config.credentials import BOT_TOKEN
from bot_handler.utils.setup_webhook import register_webhook

bot = telegram.Bot(token=BOT_TOKEN)

app = Flask(__name__)

@app.before_first_request
def enable_webhook():
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
    print(request.get_json(force=True))
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    print(f"Update: {update}")

if __name__ == "main":
    app.run(threaded=True, host="0.0.0.0", port=os.environ.get("PORT", 5000))