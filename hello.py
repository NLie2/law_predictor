from flask import Flask

from flask_cors import CORS

from encode import encode


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    example = encode("hello world")
    return "Hello!"

