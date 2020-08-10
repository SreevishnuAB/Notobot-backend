from flask import Flask


app = Flask(__name__)

if __name__ == "main":
    app.run(threaded=True, host="0.0.0.0", port=os.environ.get("PORT", 5000))