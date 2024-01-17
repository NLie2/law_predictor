from flask import Flask
from flask import Response

from flask_cors import CORS
from assess_similarities import assess_similarities

import json


app = Flask(__name__)
CORS(app)


@app.route("/")
def main():    
    # Opening JSON file
    # returns json file as a dictionary
    model_predictions = json.load(open('model_law_predictions.json'))

    
    similarity_score = assess_similarities(model_predictions)

    return {
        "model_predictions": model_predictions,
        "similarities": similarity_score
    }


