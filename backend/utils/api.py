from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Get your OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key= openai_api_key,  base_url="https://api.openai.com/v1/")


def query_gpt4(messages, model="gpt-4o", max_tokens=100):
    response = client.chat.completions.create(
        messages= messages,
        model=model, 
        max_tokens=max_tokens,
        stream = False
        )
    return response.choices[0].message

if __name__ == "__main__":
    prompt_text = "Explain the significance of machine learning in healthcare."
    messages = [
                {
                    "role": "system",
                    "content": "You are a helpful assistant",
                }, {
                    "role": "system",
                    "content": prompt_text,
                }
            ]
    print(query_gpt4(messages=messages, prompt=prompt_text, model="gpt-4o", max_tokens=150))