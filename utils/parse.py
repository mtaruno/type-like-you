import re

def get_conversation(lines, person_path, entire_conversation = False):

    parsed_data = read_and_format(person_path)

    # filtering to just the person's messages: don't think this is needed, model needs more context
    # parsed_data = [entry for entry in parsed_data if entry["name"] == 'Bryan Widjaja']

    if entire_conversation == True: 
        return base_complete_retriever(parsed_data, lines = len(parsed_data))
        

    conversation = base_retriever(parsed_data, lines) 

    return "\n".join(conversation)

def read_and_format(person_path):
    # start with whatsapp dataset
    with open(person_path, "r", encoding='utf-8') as f:
        data = f.read()

    # regex to parse data 
    pattern = re.compile(r"\[(\d{2}/\d{2}/\d{2}), (\d{2}\.\d{2}\.\d{2})\] (\w+ \w+): (.+)")

    # making into json list format
    parsed_data = []
    for line in data.split("\n"):
        match = pattern.search(line)
        if match:
            date, time, name, message = match.groups()
            entry = {
                "date": date,
                "time": time,
                "name": name,
                "message": message
            }
            parsed_data.append(entry)

    return parsed_data

def clean(data: list[str])-> list[str]:
    conversation = []
    for message in conversation: 
        pass


def base_retriever(data: list[str], lines) -> list[str]:
    conversation=[]
    # get N lines from the conversation
    for entry in data[:lines]:
        conversation.append(f"{entry['name']}: {entry['message']}")
    return conversation

def base_complete_retriever(data: list[str], lines) -> list[str]:
    conversation=[]
    # get N lines from the conversation
    for entry in data[:lines]:
        conversation.append(entry)
    return conversation

def representative_retriever(data: list[str]) -> list[str]:
    conversation = []
    return conversation