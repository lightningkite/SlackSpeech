from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/say", methods=["POST"])
def say():
    try:
        os.system("espeak '" + request.form["text"] + "'")
        return "Okay"
    except Exception as e:
        print(e)
        return "Hmmm... Something went wrong."

if __name__ == "__main__":
    app.run()