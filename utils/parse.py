import re
from typing import List


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

    # CLEANING 
    # removing the data if the message entry of the JSON object contains the U+200E character
    parsed_data = [entry for entry in parsed_data if '\u200e' not in entry["message"]]
    
    return parsed_data

def get_messages(person_path: str, lines) -> List[str]:
    parsed_data = read_and_format(person_path)

    conversation=[]
    # get N lines from the conversation
    for entry in parsed_data[:lines]:
        conversation.append(f"{entry['name']}: {entry['message']}")
    return conversation

def get_all_message_objects(person_path: str) -> List[str]:
    parsed_data = read_and_format(person_path)
    conversation=[]
    for entry in parsed_data:
        conversation.append(entry)
    return conversation

# TODO: This may be where I start to work with FAISS vector search functions
def representative_retriever(data: List[str]) -> List[str]:
    conversation = []
    return conversation