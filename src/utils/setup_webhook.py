from src.config.credentials import BOT_NAME, BOT_TOKEN, URL

def register_webhook(bot):
    status = bot.setWebhook(f"{URL}{BOT_TOKEN}")
    return status