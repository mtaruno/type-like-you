from utils.sqlite_db import initialize_database_tables, show_table, show_tables, insert_chats, delete_existing_chats, delete_existing_profile
import sqlite3
from utils.summaries import sentenceLengthDistribution, topNTokens, topEmojiDistribution, countMessages, emojiMessagesExamples
import re

def convert_to_valid_table_name(name):
    # Remove invalid characters
    name = re.sub(r'[^a-zA-Z0-9_]', '', name)
    
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    
    # Ensure the first character is a letter or underscore
    if not re.match(r'^[a-zA-Z_]', name):
        name = '_' + name
    
    # Convert to lowercase for consistency
    name = name.lower()
    
    return name


def insert_whatsapp_history_and_update_profile(whatsapp_name, whatsapp_history, emoji_examples_limit, topn_words_limit, user_slang_dictionary): 
    """
    whatsapp_history: the OG whatsapp text file formatted as a string
    """

    # delete_existing_chats(whatsapp_name)
    delete_existing_profile(whatsapp_name)    

    # table_name = convert_to_valid_table_name(whatsapp_name) # don't need it

    initialize_database_tables()  
    
    insert_chats(whatsapp_name, whatsapp_history)   
    insert_profiles(whatsapp_name,emoji_examples_limit, topn_words_limit, user_slang_dictionary) # Update the user profile



def insert_profiles(whatsapp_name, emoji_examples_limit, topn_words_limit, user_slang_dictionary):
    conn = sqlite3.connect('/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()

    try:
        # Check if the profile already exists
        cursor.execute('''
            SELECT 1 FROM profiles WHERE whatsapp_name = ?
        ''', (whatsapp_name,))
        profile_exists = cursor.fetchone()

        if profile_exists:
            print(f"Profile for {whatsapp_name} already exists.")
            
            # Delete the existing profile
            cursor.execute('''
                DELETE FROM profiles WHERE whatsapp_name = ?
            ''', (whatsapp_name,))

            return

        # Getting profile characteristics
        sentence_distribution = sentenceLengthDistribution(cursor, whatsapp_name)
        token_distribution = topNTokens(cursor, whatsapp_name, topn_words_limit)
        emoji_distribution = topEmojiDistribution(cursor, whatsapp_name)
        message_count = countMessages(cursor, whatsapp_name)
        emoji_messages_examples = emojiMessagesExamples(cursor, whatsapp_name, emoji_examples_limit)
        # user_slang_dictionary is defined in this function paramater
        
        # Inserting these profiles into the profiles table
        cursor.execute('''
            INSERT INTO profiles (
                whatsapp_name, 
                message_count, 
                sentence_distribution, 
                token_distribution, 
                user_slang_dictionary, 
                emoji_distribution, 
                emoji_messages_examples
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (whatsapp_name, message_count, sentence_distribution, token_distribution, user_slang_dictionary, emoji_distribution, emoji_messages_examples))

        conn.commit()
        print(f"Profile for {whatsapp_name} inserted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def get_profile(whatsapp_name):
    profile = {}
    
    conn = sqlite3.connect('/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT 
            whatsapp_name, 
            message_count, 
            sentence_distribution, 
            token_distribution, 
            user_slang_dictionary, 
            emoji_distribution, 
            emoji_messages_examples 
        FROM profiles 
        WHERE whatsapp_name = ?
    ''', (whatsapp_name,))
    
    row = cursor.fetchone()
    
    if row:
        profile = {
            'whatsapp_name': row[0],
            'message_count': row[1],
            'sentence_distribution': row[2],
            'token_distribution': row[3],
            'user_slang_dictionary': row[4],
            'emoji_distribution': row[5],
            'emoji_messages_examples': row[6]
        }
    
    cursor.close()
    conn.close()
    
    return profile


def store_session_message_and_response(whatsapp_name, session_id, message, response):

    conn = sqlite3.connect('/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()

    # 0 = user, 1 = talk_like_you_response
    cursor.execute('''
        INSERT INTO session_history (whatsapp_name, session_id, message, speaker)
        VALUES (?, ?, ?, 0)
    ''', (whatsapp_name, session_id, message, ))

    cursor.execute('''
            INSERT INTO session_history (whatsapp_name, session_id, message, speaker)
            VALUES (?, ?, ?, 1)
    ''', (whatsapp_name, session_id, response)) 
    conn.commit()
    cursor.close()
    conn.close()


def get_session_history(whatsapp_name, session_id):

    conn = sqlite3.connect('/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT message, speaker FROM session_history
        WHERE whatsapp_name = ? AND session_id = ?
    ''', (whatsapp_name, session_id))
    
    rows = cursor.fetchall()
    
    return rows

def format_for_gpt():
    ''' Returns a list of dictionaries in GPT API friendly format'''
    history_obj = []

    return history_obj
    


if __name__ == "__main__":
    # insert_profiles("Bryan Widjaja")
    # profile = get_profile("Bryan Widjaja")
    # for k, v in profile.items():
    #     print(f"{k}: {v}")
    whatsapp_name = "Darlin"
    session_id = 1
    print(get_session_history(whatsapp_name, session_id))