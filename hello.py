from flask import Flask
from flask_cors import CORS
from encode import encode

import json


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():    
    # Opening JSON file
    # returns json file as a dictionary
    model_predictions = json.load(open('model_law_predictions.json'))
    
    example = encode(model_predictions)
    print(example)

    return "Hello!"

