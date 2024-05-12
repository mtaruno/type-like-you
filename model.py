
# Use a pipeline as a high-level helper
from transformers import pipeline
from parse import get_conversation

pipe = pipeline("conversational", model="microsoft/phi-2", max_new_tokens = 80)

with open("prompts/imitate.txt", "r") as f:
    prompt = f.read()

# adding the conversation and message
conversation = get_conversation(lines = 30, person_path = "data/bryan.txt")
message = "Hey what are you up to bro"

print(pipe(prompt.format(conversation=conversation, message = message)))