from flask import Flask

app = Flask(__name__)

@app.route("/")
def storeafile():
    return "<p>Hello, World!</p>"

