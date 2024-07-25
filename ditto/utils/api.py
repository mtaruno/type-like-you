# import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
import yaml

if 'OPENAI_API_KEY' in os.environ:
    del os.environ['OPENAI_API_KEY']

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key= openai_api_key) # ,  base_url="https://api.openai.com/v2/"

models = {
    "gpt-4o": "gpt-4o",
    "gpt-4": "gpt-4",
    "gpt-3.5-turbo": "gpt-3.5-turbo",
}

def query_gpt4(messages, model=models["gpt-4"], max_tokens=100):
    response = client.chat.completions.create(
        messages= messages,
        model=model, 
        max_tokens=max_tokens,
        stream = False
        )

    return response.choices[0].message.content

def get_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def get_system_prompt():
    prompts = get_yaml("prompts/config.yaml")
    return prompts["SYSTEM_TEMPLATE"]

if __name__ == "__main__":

    system_prompt = "You are an intelligent assistant"

    # with open("data/thesis/report.txt", "r") as f: 
    #     report = f.read()
    
    messages = [
                {
                    "role": "system",
                    "content": system_prompt,
                }, {
                    "role": "user",
                    "content": "teach me how to use aider",
                }
            ]
    print(query_gpt4(messages=messages,  model="gpt-4o", max_tokens=4096) )