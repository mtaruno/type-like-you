'''
Helper functions that capture people's different conversational tendencies.
'''

import sqlite3
import re
from collections import Counter
import emoji



def countMessages(cursor, whatsapp_name):
    '''
    Returns the number of messages in a conversation history.
    
    Args:
        cursor (sqlite3.Cursor): SQLite cursor object.
        user_id (str): User ID of the messages to analyze.
    
    Returns:
        int: Number of total messages in the conversation history.
    '''

    cursor.execute('''
        SELECT COUNT(*) FROM whatsapp_history WHERE whatsapp_name = ?
    ''', (whatsapp_name))
    
    return cursor.fetchone()[0]

def topNTokens(cursor, whatsapp_name, n):
    '''
    Returns the top n tokens in a conversation history.
    
    Args:
        cursor (sqlite3.Cursor): SQLite cursor object.
        user_id (str): User ID of the messages to analyze.
        n (int): Number of top tokens to return.
    
    Returns:
        List[Tuple[str, int]]: List of tuples containing the top n tokens and their counts.
    '''
    cursor.execute('''
        SELECT message FROM whatsapp_history WHERE whatsapp_name = ?
    ''', (whatsapp_name))
    
    messages = cursor.fetchall()
    all_tokens = []
    
    for message in messages:
        tokens = re.findall(r'\b\w+\b', message[0].lower())  # Tokenize the message
        all_tokens.extend(tokens)
    
    token_counts = Counter(all_tokens)
    top_tokens = token_counts.most_common(n)
    
    return top_tokens

def topEmojiDistribution(cursor, imitated_person_name, user_id):
    '''
    Returns the top emoji distribution in a conversation history in string format.
    
    Args:
        cursor (sqlite3.Cursor): SQLite cursor object.
        user_id (str): User ID of the messages to analyze.
    
    Returns:
        str: String representation of the top emoji distribution.
    '''

    cursor.execute('''
        SELECT message FROM whatsapp_history WHERE whatsapp_name = ? 
    ''', (whatsapp_name))
    
    messages = cursor.fetchall()
    all_emojis = []
    
    for message in messages:
        all_emojis.extend([char for char in message[0] if emoji.is_emoji(char)])
    
    emoji_counts = Counter(all_emojis)
    top_emojis = emoji_counts.most_common()
    
    return ', '.join([f'{emj}: {count}' for emj, count in top_emojis])

def sentenceLengthDistribution(cursor, whatsapp_name, user_id):
    """
    Returns the sentence length distribution in a conversation history in string format.
    
    Args:
        cursor (sqlite3.Cursor): SQLite cursor object.
        user_id (str): User ID of the messages to analyze.
    
    Returns:
        str: String representation of the sentence length distribution.
    """
    cursor.execute('''
        SELECT message FROM whatsapp_history WHERE whatsapp_name = ?
    ''', (whatsapp_name))
    
    messages = cursor.fetchall()
    sentence_lengths = []
    
    for message in messages:
        sentences = re.split(r'[.!?]', message[0])  # Split the message into sentences
        sentence_lengths.extend([len(sentence.split()) for sentence in sentences if sentence.strip()])
    
    length_counts = Counter(sentence_lengths)
    length_distribution = sorted(length_counts.items())
    
    return ', '.join([f'{length} words: {count}' for length, count in length_distribution])

def sample_conversation(whatsapp_name: str, message_count: int):
    """
    Retrieve sample messages (amount specified by message_count) from the conversation history of the user.database of the user. 
    """
    pass

# Language Switching
def languageTokensFrequency(user_id):
    """
    Return a dictionary of how many tokens of each language are used in the conversation history.
    """
    pass

def langaugeSwitchFrequency(user_id): 
    """
    Returns all the cases where more than one language is used in the conversation line.
    """
    pass


if __name__ == "__main__":
    # Example Usage
    conn = sqlite3.connect("/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db")
    cursor = conn.cursor()

    whatsapp_name= 'bwidjaja'

    print(topNTokens(cursor, whatsapp_name, 30))
    print(topEmojiDistribution(cursor, whatsapp_name))
    print(sentenceLengthDistribution(cursor, whatsapp_name))
    
    conn.close()