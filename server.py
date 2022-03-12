from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/posts")
def posts():
    try:
        with open("./posts.json") as fp:
            return fp.read()
    except FileNotFoundError:
        return "no posts found"


@app.route("/reports")
def reports():
    try:
        with open("./reports.json") as fp:
            return fp.read()
    except FileNotFoundError:
        return "no reports found"