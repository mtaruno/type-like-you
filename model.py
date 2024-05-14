from transformers import pipeline, Conversation
from parse import get_conversation

# Initialize the conversational pipeline
pipe = pipeline("conversational", model="microsoft/phi-2", max_new_tokens=80)

with open("prompts/imitate.txt", "r") as f:
    prompt = f.read()

# Add the conversation and message
conversation_lines = get_conversation(lines=30, person_path="data/bryan.txt")
message = "Hey, what are you up to bro"

# Assuming `get_conversation` returns a list of strings (lines of the conversation)
conversation = Conversation()
for line in conversation_lines:
    conversation.add_user_input(line)
conversation.add_user_input(message)

formatted_prompt = prompt.format(conversation=conversation, message=message)

# Generate the response
response = pipe([conversation])
print(response)
