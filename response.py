from utils.parse import get_conversation
from utils.api import query_gpt4
import argparse


def get_response(system_response, user_message):

    messages = []

    # add system content
    messages.append(system_response)
    # add user content
    messages.append(user_message)
    
    return query_gpt4(messages=messages, model="gpt-4o", max_tokens=150).content


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process some message content.")
    parser.add_argument('--message', '-m', type=str, required=True, help='The message content to process')
    args = parser.parse_args()
    message = args.message

    # get prompt
    with open("prompts/imitate.txt", "r") as f:
        prompt = f.read()
    
    # get conversation to add to prompt
    conversation = get_conversation(lines=50, person_path="data/bryan.txt")
    
    formatted_prompt = prompt.format(conversation=conversation, message=message)
    print(formatted_prompt)

    print(f"Tokens: {len(formatted_prompt.split())}") # gpt4o max context length is 128k

    sys_prompt = {
                    "role": "system",
                    "content": formatted_prompt}
    message_obj = {
                    "role": "user",
                    "content": message,
                }
   
    response = get_response(sys_prompt,message_obj)
    print(response)

