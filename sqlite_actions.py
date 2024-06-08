from utils.sqlite_db import *
from utils.summaries import sentenceLengthDistribution, wordCountDistribution, wordFrequencyDistribution, wordLengthDistribution


def insert_whatsapp_db(whatsapp_name): 

    initialize_database_tables()  
    
    insert_chats(whatsapp_name, "/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/bryan.txt")

    show_tables()
    show_table('conversations')
    show_table('session_conversations')

    conn.close()

def insert_profiles(whatsapp_name):
    pass


def get_profile(whatsapp_name):
    profile = {}

    

    return profile



if __name__ == "__main__":
    pass 