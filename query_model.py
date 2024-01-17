import pandas as pd 
from dotenv import load_dotenv
from openai import OpenAI
import os


# Load dataset
ethical_dataset = pd.read_csv('ethical_dataset.csv', sep=";")
question = ethical_dataset.iloc[10]['Question/Case Description']
print(question, type(question))

#Give one line to chatgpt
load_dotenv()



OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    # {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": question}
  ]
)

print(completion.choices[0].message)