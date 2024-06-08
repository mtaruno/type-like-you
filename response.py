from inference.api import query_gpt4
import argparse
import yaml

def get_yaml(file_path : str) -> dict:
    with open(file_path, "r") as f:
        prompts = yaml.safe_load(f)

    print(prompts[''])


    return prompts




def get_response(user_message : str) -> str:
    messages = []

    messages.append(initialize_conversation())

    # add user content
    messages.append(user_message)
    
    return query_gpt4(messages=messages, model="gpt-4o", max_tokens=1000).content


def initialize_conversation():
    '''Provide the LLM with the system prompt'''
   # get prompt
    with open("prompts/imitate.txt", "r") as f:
        prompt = f.read()
    
    # get conversation to add to prompt
    # conversation = get_messages(person_path = person_path, lines=50)
        


    # get all profile variables
    profile = get_profile()    
    
    formatted_prompt = prompt.format(conversation=conversation, person = person_name)
    print(formatted_prompt)

    print(f"Tokens: {len(formatted_prompt.split())}") # gpt4o max context length is 128k
    
    sys_obj ={"role": "system",
                    "content": formatted_prompt}

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

