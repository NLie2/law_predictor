from flask import Flask
from flask import Response

from flask_cors import CORS
from assess_similarities import assess_similarities, assess_similarity, assess_multiple_choice
from visualize_most_similar_sentences import visualize_most_similar_sentences
from query_model import query_model

import json

import pandas as pd

# import example answer for testing 
# * From row 6 in the dataset
from example_answer import answer


app = Flask(__name__)
CORS(app)


# Load dataset
ethical_dataset = pd.read_csv('ethical_dataset.csv', sep=";")
selected = ethical_dataset.iloc[6]


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
    model_answer = answer
  
    # print(selected_type)
    if selected_type == "multiple choice":
        scores = assess_multiple_choice(model_answer= model_answer, gold_answer=selected_answer )
        print(scores)

    # ! Its possible you get an error here because visualize similar sentences only works right now if one answer has len = 1  
    else:
        scores = assess_similarity(model_answer= model_answer, gold_answer=selected_answer )
        most_similar_sentences = visualize_most_similar_sentences(model_answer= model_answer, gold_answer=selected_answer)

    return {
        "question": selected_question,
        "model_answer": model_answer,
        "gold_answer": selected_answer,
        "score": str(scores['cosine_model_gold']),
        "baseline": str(scores['cosine_baseline'])
    }

