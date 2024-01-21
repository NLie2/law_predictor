from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

examples = {
      'example1': {
          'model_answer': """The first step is to create a new directory for your project. You can do this by running the following command in your terminal: mkdir my-project-name cd my-project-name""",
          'gold_answer': """The first step is to create a new directory for your project. You can do this by running the following command in your terminal: mkdir my-project-name cd my-project-name"""
      },
      'example2': {
          'model_answer': """The first step is to create a new directory for your project. You can do this by running the following command in your terminal: mkdir my-project-name cd my-project-name""",
          'gold_answer': """The first step is to create a new directory for your project. You can do this by running the following command in your terminal: mkdir my-project-name cd my-project-name"""
      },
      'example3': {
          'model_answer': """The first step is to create a new directory for your project. You can do this by running the following command in your terminal: mkdir my-project-name cd my-project-name""",
          'gold_answer': """The first step is to create a new directory for your project. You can do this by running the following command in your terminal: mkdir my-project-name cd my-project-name"""
      },
      'example4': {
          'model_answer': """The first step is to create a new directory for your project. You can do this by running the following command in your terminal: mkdir my-project-name cd my-project-name""",
          'gold_answer': """The first step is to create a new directory for your project. You can do this by running the following command in your terminal: mkdir my-project-name cd my-project-name"""
      }
  }

def visualize_most_similar_sentences(example):

  # Split outputs into sentences
  remove_spaces = [sentence.replace("  ", "") for sentence in example["model_answer"].split('.')]
  cleaned_modeloutput = [sentence.replace('\n', '') for sentence in remove_spaces]

  remove_spaces = [sentence.replace("  ", "") for sentence in example["gold_answer"].split('.')]
  cleaned_goldanswer = [sentence.replace('\n', '') for sentence in remove_spaces] 


  embeddings1 = model.encode(cleaned_modeloutput, convert_to_tensor=True)
  embeddings2 = model.encode(cleaned_goldanswer, convert_to_tensor=True)

  # Output all possible pairs of sentences with their score
  cosine_scores = [[0 for _ in range(len(cleaned_goldanswer))] for _ in range(len(cleaned_modeloutput))]
  for i in range(len(cleaned_goldanswer)):
      for j in range(len(cleaned_modeloutput)):
        
        #calculate cosine and convert to float with .item()
        cosine_scores[j][i] = util.cos_sim(embeddings2[i], embeddings1[j]).item()

        print("{} \t\t {} \t\t Score: {:.4f}".format(cleaned_modeloutput[j], cleaned_goldanswer[i], cosine_scores[j][i]))
      print("")


  #Find the pairs with the highest cosine similarity scores
  pairs = []
  for i in range(len(cosine_scores[0])):
      for j in range(len(cosine_scores[1])):
          pairs.append({'index': [i, j], 'score': cosine_scores[i][j]})

  #Sort scores in decreasing order
  pairs = sorted(pairs, key=lambda x: x['score'], reverse=True)

  for pair in pairs[0:10]:
      i, j = pair['index']
      print("{} \t\t {} \t\t Score: {:.4f}".format(cleaned_modeloutput[i], cleaned_goldanswer[j], pair['score']))


visualize_most_similar_sentences(examples['example1' ])