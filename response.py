from utils.parse import get_conversation
from utils.api import query_gpt4
import argparse


def get_history():
    pass

def get_response(user_message : str, start : bool) -> str:
    # messages = get_history
    messages = []

    if start:
        messages.append(initialize_conversation("data/bryan.txt"))

    # add user content
    messages.append(user_message)
    
    return query_gpt4(messages=messages, model="gpt-4o", max_tokens=1000).content

def initialize_conversation(person_path = "data/bryan.txt", person_name = "Bryan"):
    ''' Gives the first sys response which is the prompt'''
   # get prompt
    with open("prompts/imitate.txt", "r") as f:
        prompt = f.read()
    
    # get conversation to add to prompt
    conversation = get_conversation(person_path = person_path, lines=50)
    formatted_prompt = prompt.format(conversation=conversation, person = person_name)
    print(formatted_prompt)

    print(f"Tokens: {len(formatted_prompt.split())}") # gpt4o max context length is 128k
    
    sys_obj ={"role": "system",
                    "content": formatted_prompt}
    
    print(sys_obj)    

    return sys_obj

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some message content.")
    parser.add_argument('--message', '-m', type=str, required=True, help='The message content to process')
    args = parser.parse_args()
    message = args.message

    message_obj = {
                "role": "user",
                "content": message,
            }   
    
    response = get_response(message_obj, start = True)

    print("==" * 10)
    print(response)

