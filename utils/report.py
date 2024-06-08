from utils.parse import get_all_message_objects
from inference.api import query_gpt4
import argparse




def generate_emoji_report():
    pass


# DEPRACATED: The LLM is incapable of generating an entire summary of all the aspects at once. 
def generate_report(person_path):
    # get prompt
    with open("prompts/habits.txt", "r") as f:
        prompt = f.read()
    
    # get conversation to add to prompt
    conversation = get_all_message_objects(person_path=person_path)
    # adding user message 
    formatted_prompt = prompt.format(conversation=conversation)
    print(formatted_prompt)
    print(f"Tokens: {len(formatted_prompt.split())}") # gpt4o max context length is 128k

    messages = [
                {
                    "role": "system",
                    "content": formatted_prompt,
                }
            ]
    
    return query_gpt4(messages=messages, model="gpt-4o", max_tokens=5000).content


if __name__ == "__main__":
    with open ("log/report.txt", "w") as f:
        f.write(generate_report(person_path="data/jamesmarshall.txt"))