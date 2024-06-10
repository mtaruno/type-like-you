import re
from typing import List
import json 


def read_file(person_path):
    with open(person_path, "r", encoding='utf-8') as f:
        data = f.read()
    return data

def format_data(whatsapp_history: str):
    # regex to parse data 
    # pattern = re.compile(r"\[(\d{2}/\d{2}/\d{2}), (\d{2}\.\d{2}\.\d{2})\] (\w+ \w+): (.+)")
    pattern = re.compile(r"\[(\d{2}/\d{2}/\d{2}), (\d{2}\.\d{2}\.\d{2})\] ([^:]+): (.+)")
    # making into json list format
    parsed_data = []
    for line in whatsapp_history.split("\n"):
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
    # removing the data if the message entry of the JSON object contains the U+200E character or contains external content
    parsed_data = [entry for entry in parsed_data if '\u200e' not in entry["message"] or contains_external_content(entry["message"])]
    
    return parsed_data

def contains_external_content(message):
    return bool(re.search(r'http[s]?://|www\.', message))

def txt_to_json(whatsapp_name,person_path):
    # stores the txt file into a json file
    history = read_file(person_path)
    data = { "whatsapp_name": whatsapp_name,
        "whatsapp_history": history
    }
    json_path = f"{person_path}.json"
    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Data has been written to {json_path}")
    

def get_messages(person_path: str, lines) -> List[str]:
    parsed_data = format_data(read_file(person_path))

    conversation=[]
    # get N lines from the conversation
    for entry in parsed_data[:lines]:
        conversation.append(f"{entry['name']}: {entry['message']}")
    return conversation

def get_all_message_objects(whatsapp_history_path: str) -> List[str]:
    parsed_data = format_data(read_file(whatsapp_history_path))
    conversation=[]
    for entry in parsed_data:
        conversation.append(entry)
    return conversation

# TODO: This may be where I start to work with FAISS vector search functions
def representative_retriever(data: List[str]) -> List[str]:
    conversation = []
    return conversation


if __name__ == "__main__":
    whatsapp_name = "Eggy Alicloud"
    txt_to_json(whatsapp_name, "data/eggy.txt")
    # print(set([i["name"] for i in get_all_message_objects("data/darlin.txt")]))