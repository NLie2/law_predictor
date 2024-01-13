
from sentence_transformers import SentenceTransformer, util
import torch

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

def encode( string):
  embedding = model.encode(string, convert_to_tensor=True)
  return embedding