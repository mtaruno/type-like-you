import re
from typing import List
import json 
from dataclasses import dataclass


def read_file(person_path):
   
    return data


# NOTE: Profile class not implemented yet
@dataclass
class Profile:
    whatsapp_name: str
    person_path: str
    pattern: str
    
    def test_parser(self):
        pass
    


def format_data(whatsapp_history: str):
    # regex to parse data 
    pattern = re.compile(r"\[(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}:\d{2} (?:AM|PM))\] ([^:]+): (.+)") # metilda
    # pattern = re.compile(r"(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}(?:AM|PM|:\d{2})?) - (.*?): (.*)") # cherry
    # pattern = re.compile(r"\[(\d{2}/\d{2}/\d{2}), (\d{2}\.\d{2}\.\d{2})\] (\w+ \w+): (.+)")
    # pattern = re.compile(r"\[(\d{1,2}/\d{1,2}/\d{2,4}),\s+(\d{1,2}:\d{2})\s*-\s*([^:]+): (.+)") # goga
    # pattern = re.compile(r"\[(\d{1,2}/\d{1,2}/\d{2,4}),\s+(\d{1,2}:\d{2}:\d{2}[\u202f\s]*(?:AM|PM))\] ([^:]+): (.+)")  # yaoming
    # pattern = re.compile(r"\[(\d{2}/\d{2}/\d{2}), (\d{2}\.\d{2}\.\d{2})\] ([^:]+): (.+)") # matt
    # pattern = re.compile(r"\[(\d{1,2}/\d{1,2}/\d{2,4}),\s+(\d{1,2}:\d{2}:\d{2}\s*(?:AM|PM)?)\] ([^:]+): (.+)") # trisha

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
    parsed_data = [entry for entry in parsed_data if '\u200e' not in entry["message"] and 'omitted' not in entry["message"]] # or contains_external_content(entry["message"]
    assert len(parsed_data) > 0 , "No data found in the file, please fix the WhatsApp parser"
    return parsed_data


# def txt_to_json(whatsapp_name, person_path):
#     # Read the text file
#     with open(person_path, 'r', encoding='utf-8') as file:
#         whatsapp_history = file.read()
    
#     # Format the data
#     formatted_data = format_data(whatsapp_history)
    
#     # Create the final JSON structure
#     data = {
#         "whatsapp_name": whatsapp_name,
#         "whatsapp_history": formatted_data
#     }
    
#     # Write to a JSON file
#     json_path = f"{person_path}.json"
#     with open(json_path, "w", encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)
    
#     print(f"Data has been written to {json_path}")
    

def contains_external_content(message):
    return bool(re.search(r'http[s]?://|www\.', message))

# def txt_to_json(whatsapp_name,person_path):
#     # stores the txt file into a json file
#     history = read_file(person_path)
#     data = { "whatsapp_name": whatsapp_name,
#         "whatsapp_history": history
#     }
#     json_path = f"{person_path}.json"
#     with open(json_path, "w") as f:
#         json.dump(data, f, indent=4)

#     print(f"Data has been written to {json_path}")
    

def txt_to_json(whatsapp_name, person_path):
    history_lines = read_file(person_path)
    messages = history_lines
    
    data = {
        "whatsapp_name": whatsapp_name,
        "user_slang_dictionary": "" ,
        "whatsapp_history": messages
    }
    
    json_path = f"{person_path}.json"
    with open(json_path, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

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


if __name__ == "__main__":

    mum = Profile(whatsapp_name = "Mum",person_path= "data/mum.txt", pattern = re.compile(r"\[(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}:\d{2} (?:AM|PM))\] ([^:]+): (.+)"))
    
    
    with open("/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/boas.txt", "r", encoding='utf-8') as f:
        data = f.read()

    with open("/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/boas.json", "w") as f:
        # store it all in a string
        json.dump(data, f, ensure_ascii=False, indent=4)


