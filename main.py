from flask import Flask
from flask import Response

from flask_cors import CORS
from assess_similarities import assess_similarities, assess_similarity, assess_multiple_choice
from query_model import query_model

import json

import pandas as pd


app = Flask(__name__)
CORS(app)


# Load dataset
ethical_dataset = pd.read_csv('ethical_dataset.csv', sep=";")
selected = ethical_dataset.iloc[11]


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
    selected_question = selected['Question/Case Description']
    selected_answer = selected['Answer/Judgement']
    selected_type = selected['Type']

    ## ! Comment out to prevent unnecessary API calls
    #model_answer = query_model(question)
    #print(model_answer)
    
    
    # model_answer = "A: Listen to the patient's wife's wishes and withdraw care"
    model_answer = json.load(open('example_answer.json'))['answer']
  
    # scores = assess_similarity(model_answer= model_answer, gold_answer=ethical_dataset.iloc[11]['Answer/Judgement'] )
    # print(selected_type)
    if selected_type == "multiple choice":
        scores = assess_multiple_choice(model_answer= model_answer, gold_answer=selected_answer )
        print(scores)

    return {
        "question": ethical_dataset.iloc[11]['Question/Case Description'],
        "model_answer": model_answer,
        "gold_answer": ethical_dataset.iloc[11]['Answer/Judgement'],
        "score": str(scores['cosine_model_gold']),
        "baseline": str(scores['cosine_baseline'])
    }

