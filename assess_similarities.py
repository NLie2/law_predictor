
from sentence_transformers import SentenceTransformer, util
import torch
import numpy as np

embeddings = {"hello": "world"}

# for key, example in examples.items(): 
#   embeddings[key] = {"model_answer": model.encode(example["model_answer"], convert_to_tensor=True)}
#   embeddings[key]["gold_answer"] = model.encode(example["gold_answer"], convert_to_tensor=True)

# # calculate similarity of entire document
# for key, example in embeddings.items(): 
#   example["cosine_model_gold"] = util.cos_sim(example['model_answer'], example['gold_answer'])
#   example["cosine_documents_perfect"] = util.cos_sim(example['model_answer'], example['model_answer'])
#   example["cosine_documents_baseline"] = util.cos_sim(example['model_answer'], embeddings['example4']['model_answer']) 

#   print("consine: ",example['cosine_model_gold'])
#   print("perfect:",example['cosine_documents_perfect'])
#   print("baseline: ",example['cosine_documents_baseline'])
#   print()
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def assess_similarities( model_predictions ):
  embeddings = {}

  for key, example in model_predictions.items(): 
    embeddings[key] = {"model_answer": model.encode(example["model_answer"], convert_to_tensor=True)}
    embeddings[key]["gold_answer"] = model.encode(example["gold_answer"], convert_to_tensor=True)
  

  for key, example in embeddings.items():
      # print(key)
      example["cosine_model_gold"] = float(util.cos_sim(example['model_answer'], example['gold_answer']).numpy()[0][0])
      example["cosine_documents_perfect"] = float(util.cos_sim(example['model_answer'], example['model_answer']).numpy()[0][0])
      example["cosine_documents_baseline"] = float(util.cos_sim(example['model_answer'], embeddings['example4']['model_answer']).numpy()[0][0])
      
      print("consine: ", example['cosine_model_gold'])
      print("perfect:",example['cosine_documents_perfect'])
      print("baseline: ",example['cosine_documents_baseline'])


  # for each example in embeddings, only return cosine_model_gold, cosine_documents_perfect, cosine_documents_baseline
  filtered_embeddings = {key: {k: value for k,value in example.items() if k in ['cosine_model_gold', 'cosine_documents_perfect', 'cosine_documents_baseline']} for key, example in embeddings.items()}

  return filtered_embeddings