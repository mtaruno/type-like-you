from inference.api import query_gpt4, get_system_prompt
import argparse
from sqlite_actions import get_profile


def get_response(user_message : str, whatsapp_name : str) -> str:
    messages = []

    messages.append(initialize_conversation(whatsapp_name))

    # add user content
    messages.append(user_message)
    
    return query_gpt4(messages=messages, model="gpt-4o", max_tokens=1000)


def initialize_conversation(whatsapp_name):
    '''Provide the LLM with the system prompt'''
    # get conversation to add to prompt
    # conversation = get_messages(person_path = person_path, lines=50)

    # get all profile variables
    profile = get_profile(whatsapp_name)    
    prompt = get_system_prompt()

    # adding it to the system prompt
    system_prompt = prompt.format(
        whatsapp_name = profile["whatsapp_name"],
        message_count = profile["message_count"],
        sentence_distribution = profile["sentence_distribution"],
        token_distribution = profile["token_distribution"],
        user_slang_dictionary = profile["user_slang_dictionary"],
        emoji_distribution = profile["emoji_distribution"],
        emoji_messages_examples = profile["emoji_messages_examples"],
        # example_conversation = profile["example_conversation"]
    )
    print(f"System Prompt: {system_prompt}")
    print(f"Tokens: {len(system_prompt.split())}") # gpt4o max context length is 128k
    
    sys_obj ={"role": "system",
                    "content": system_prompt}

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
    
    response = get_response(message_obj, "Bryan Widjaja")

    print("==" * 10)
    print(response)

