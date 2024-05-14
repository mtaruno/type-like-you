import re

def get_conversation(lines, person_path):
    # start with whatsapp dataset
    with open(person_path, "r") as f:
        data = f.read()

    # regex to parse data 
    pattern = re.compile(r"\[(\d{2}/\d{2}/\d{2}), (\d{2}\.\d{2}\.\d{2})\] (\w+ \w+): (.+)")

    # Extracting and organizing the data
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

    # filtering to just the person's messages
    parsed_data = [entry for entry in parsed_data if entry["name"] == 'Bryan Widjaja"]

    conversation = []
    # get N lines from the conversation
    for entry in parsed_data[:lines]:
        conversation.append(f"{entry['name']}: {entry['message']}")

    return conversation