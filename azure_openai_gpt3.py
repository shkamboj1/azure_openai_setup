import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = os.getenv('OPENAI_API_TYPE')
openai.api_version = os.getenv('OPENAI_API_VERSION')

deployment_name= os.getenv('DEPLOYMENT_NAME') #This will correspond to the custom name you chose for your deployment when you deployed a model. 

# Send a completion call to generate an answer

prompt = 'Write a tagline for an ice cream shop. '
print(f"Prompt : {prompt}")
response = openai.Completion.create(engine=deployment_name, prompt=prompt, max_tokens=10)
text = response['choices'][0]['text']
print(f"output: {text}")