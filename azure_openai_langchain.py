import os
import openai

from dotenv import load_dotenv
load_dotenv()

azure_openai_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')

os.environ["OPENAI_API_TYPE"] = os.getenv('OPENAI_API_TYPE')
os.environ["OPENAI_API_VERSION"] = os.getenv('OPENAI_API_VERSION')
os.environ["OPENAI_API_BASE"] = azure_openai_endpoint[:-1] if azure_openai_endpoint.endswith('/') else azure_openai_endpoint
os.environ["OPENAI_API_KEY"] = os.getenv('AZURE_OPENAI_KEY')
deployment_name = os.getenv('DEPLOYMENT_NAME')

from langchain.llms import AzureOpenAI


# Create an instance of Azure OpenAI
# Replace the deployment name with your own
llm = AzureOpenAI(
    deployment_name=deployment_name
)

print(llm("Tell me a joke"))

