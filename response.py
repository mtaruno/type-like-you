from utils.parse import get_conversation
from utils.api import query_gpt4


def get_response(message):
    # get prompt
    with open("prompts/imitate.txt", "r") as f:
        prompt = f.read()

    # get conversation to add to prompt
    conversation = get_conversation(lines=30, person_path="data/bryan.txt")

    # adding user message 
    formatted_prompt = prompt.format(conversation=conversation, message=message)
    print(formatted_prompt)

    messages = [
                {
                    "role": "system",
                    "content": formatted_prompt,
                }, 
                {
                    "role": "user",
                    "content": message,
                }
            ]
    return query_gpt4(messages=messages, model="gpt-4o", max_tokens=150).content


if __name__ == "__main__":
    message =  "Hey, what are you up to bro. What did u do today?"
    response = get_response(message)
    print(response)