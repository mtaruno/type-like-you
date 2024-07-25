
import re

def format_data(whatsapp_history: str):
    # Regex pattern to parse the chat data
    pattern = re.compile(r"\[(\d{1,2}/\d{1,2}/\d{2,4}),\s*(\d{1,2}:\d{2})\s*-\s*([^:]+): (.+)")


    # Making into JSON list format
    parsed_data = []
    current_message = None

    for line in whatsapp_history.split("\n"):
        match = pattern.match(line)
        if match:
            if current_message:
                parsed_data.append(current_message)
            date, time, name, message = match.groups()
            current_message = {
                "date": date,
                "time": time,
                "name": name,
                "message": message
            }
        elif current_message:
            current_message["message"] += "\n" + line.strip()
    
    # Append the last message
    if current_message:
        parsed_data.append(current_message)

    # CLEANING
    # Removing the data if the message entry of the JSON object contains the U+200E character or contains external content
    parsed_data = [entry for entry in parsed_data if '\u200e' not in entry["message"] and 'omitted' not in entry["message"]]
    assert len(parsed_data) > 0, "No data found in the file, please fix the WhatsApp parser"
    return parsed_data

# Sample data
whatsapp_history = """7/10/22, 21:02 - Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.
7/10/22, 21:02 - Goga Pogosyan: Good day Stephen, Ivan gave me your contact information and told me that you will get in touch tomorrow, i am looking forward to our conversation. 
I have only one request as of now, could you please let me know at least 2 hours in advance, so, i can put it into my schedule.
Thank You
7/10/22, 23:59 - Stephen AOK Freight: I will rea h ou tomorrow  and we cN discuss what your company can do for us.
7/11/22, 23:20 - Goga Pogosyan: Good morning Stephen, are we good for today?
7/11/22, 23:32 - Stephen AOK Freight: Could you send me information about your company and what services you offer?
7/11/22, 23:32 - Stephen AOK Freight: My email is sr@aokfreight.com
7/11/22, 23:33 - Stephen AOK Freight: If you have a few voice demos of your staff?
7/11/22, 23:33 - Goga Pogosyan: Stephen if possible, i would like to explain it to you during a call
7/11/22, 23:38 - Goga Pogosyan: The voice memos and our company ibformation are not an issue at all
7/11/22, 23:40 - Goga Pogosyan: The operations we have active right now are related to the same industry as yours but, different category.
7/11/22, 23:41 - Goga Pogosyan: If we could get on the phone for 5 minutes, that will be more than enough to tell you all about it.
7/11/22, 23:42 - Stephen AOK Freight: Can we do w web call?
7/11/22, 23:42 - Stephen AOK Freight: I can do a video call here"""

# Test the function
parsed_data = format_data(whatsapp_history)
for entry in parsed_data:
    print(entry)
