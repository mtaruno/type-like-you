with open("prompts/imitate.txt", "r") as f:
    prompt = f.read()

prompt = prompt.format(conversation="abc123")

print(prompt)
