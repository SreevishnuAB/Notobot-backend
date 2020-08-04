from flask import Flask, request
from logging.config import dictConfig
import telegram
from bot_handler.config.credentials import BOT_TOKEN

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

@app.route("/")
def index():
    app.logger.info(BOT_TOKEN)
    if BOT_TOKEN != None:
        return {"message": "Bot token loaded successfully"}
    else:
        return {"error": "Something went wrong"}

if __name__ == "main":
    app.run(threaded=True)