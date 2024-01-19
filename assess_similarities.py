
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

baseline_string = "The regulation states that a patient's consent to medical treatment must be informed, freely given, and without any form of pressure or deception. It must also be a well-considered declaration of the patient's will, understanding both the benefits and risks involved. In this case, the regulation would guide the physician to take additional steps to ensure that the patient fully understands the experimental nature of the treatment and all potential risks, thereby safeguarding the patient's right to self-determination. The regulation states that a patient's consent to medical treatment must be informed, freely given, and without any form of pressure or deception. It must also be a well-considered declaration of the patient's will, understanding both the benefits and risks involved. In this case, the regulation would guide the physician to take additional steps to ensure that the patient fully understands the experimental nature of the treatment and all potential risks, thereby safeguarding the patient's right to self-determination. If the patient, after receiving all the necessary information in a manner they can comprehend, still decides to proceed with the treatment, then the physician can administer it in good conscience, knowing that the consent is informed and valid according to the regulation. If the patient's understanding remains inadequate, the physician should refrain from proceeding until the patient reaches a well-considered decision."

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def assess_similarity( model_answer, gold_answer ):
  embedding_model_answer = model.encode(model_answer, convert_to_tensor=True)
  embedding_gold_answer = model.encode(gold_answer, convert_to_tensor=True)
  embedding_baseline = model.encode(baseline_string, convert_to_tensor=True)

  # print(embedding_gold_answer, embedding_model_answer)
  cosine_model_gold = ""
  cosine_perfect = ""
  cosine_baseline = ""
  
  cosine_model_gold = round(float(util.cos_sim(embedding_model_answer, embedding_gold_answer).numpy()[0][0]), 3)
  cosine_perfect = round(float(util.cos_sim(embedding_model_answer, embedding_model_answer).numpy()[0][0]), 3) 
  cosine_baseline = round(float(util.cos_sim(embedding_model_answer, embedding_baseline).numpy()[0][0]), 3)

  return ({'cosine_model_gold': cosine_model_gold, 'cosine_perfect': cosine_perfect, 'cosine_baseline': cosine_baseline})


def assess_similarities( model_predictions ):
  embeddings = {}

  for key, example in model_predictions.items(): 
    embeddings[key] = {"model_answer": model.encode(example["model_answer"], convert_to_tensor=True)}
    embeddings[key]["gold_answer"] = model.encode(example["gold_answer"], convert_to_tensor=True)
  

  for key, example in embeddings.items():
      # print(key)
      example["cosine_model_gold"] = round(float(util.cos_sim(example['model_answer'], example['gold_answer']).numpy()[0][0]), 3)
      example["cosine_documents_perfect"] = round(float(util.cos_sim(example['model_answer'], example['model_answer']).numpy()[0][0]), 3)
      example["cosine_documents_baseline"] = round(float(util.cos_sim(example['model_answer'], embeddings['example4']['model_answer']).numpy()[0][0]), 3)
      
      print("consine: ", example['cosine_model_gold'])
      print("perfect:",example['cosine_documents_perfect'])
      print("baseline: ",example['cosine_documents_baseline'])


  # for each example in embeddings, only return cosine_model_gold, cosine_documents_perfect, cosine_documents_baseline
  filtered_embeddings = {key: {k: value for k,value in example.items() if k in ['cosine_model_gold', 'cosine_documents_perfect', 'cosine_documents_baseline']} for key, example in embeddings.items()}

  return filtered_embeddings