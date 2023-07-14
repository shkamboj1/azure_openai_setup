# For GPT3.5 and 4

import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = os.getenv('OPENAI_API_TYPE')
openai.api_version = os.getenv('OPENAI_API_VERSION')
deployment_name= os.getenv('DEPLOYMENT_NAME') 

response = openai.ChatCompletion.create(
    engine=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ]
)
print(response['choices'][0]['message']['content'])