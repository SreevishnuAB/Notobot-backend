from flask import Flask


app_instance = Flask(__name__)

if __name__ == "main":
    app_instance.run(threaded=True, host="0.0.0.0", port=os.environ.get("PORT", 5000))