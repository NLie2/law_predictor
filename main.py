from flask import Flask
from flask import Response

from flask_cors import CORS
from assess_similarities import assess_similarities, assess_similarity
from query_model import query_model

import json

import pandas as pd


app = Flask(__name__)
CORS(app)


# Load dataset
ethical_dataset = pd.read_csv('ethical_dataset.csv', sep=";")
question = ethical_dataset.iloc[11]['Question/Case Description']


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


@app.route("/query")
def query():    

    # query model with question 
    question = ethical_dataset.iloc[11]['Question/Case Description']

    ## ! Comment out to prevent unnecessary API calls
    #model_answer = query_model(question)
    #print(model_answer)
    
    
    model_answer = "The most appropriate next step in this situation is to (E) contact the ethics committee. Given the patient's unstable condition and the discrepancy between the patient's written advance directive and the power of attorney's wishes, it is important to involve an ethics committee to provide guidance and help resolve the ethical dilemma."
    
    scores = assess_similarity(model_answer= model_answer, gold_answer=ethical_dataset.iloc[11]['Answer/Judgement'] )

    return {
        "question": ethical_dataset.iloc[11]['Question/Case Description'],
        "model_answer": model_answer,
        "gold_answer": ethical_dataset.iloc[11]['Answer/Judgement'],
        "score": scores['cosine_model_gold'],
        "baseline": scores['cosine_baseline']
    }

