import sqlite3
from utils.parse import get_all_message_objects, format_data, format_chinese_data
import re

# Example chat objects
# chats = [
#     {'role': 'system', 'content': "Yo what's up bro?"},
#     {'role': 'user', 'content': "remember last time we talked about airplanes, tell me how those work"}
# ]

# Function to validate table name
def validate_table_name(table_name):
    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', table_name):
        return True
    else:
        raise ValueError("Invalid table name")

def delete_existing_chats(whatsapp_name):
    conn = sqlite3.connect('/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()
    # Check if whatsapp_name already exists in whatsapp_history and removes entries if it does
    cursor.execute('''
    DELETE FROM whatsapp_history WHERE whatsapp_name=?;
    ''', (whatsapp_name,))

    print(f"Chats with whatsapp name {whatsapp_name} deleted from database.")
    conn.commit()
    cursor.close()
    conn.close()

def delete_user_history(whatsapp_name):
    conn = sqlite3.connect('/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()
    # Check if whatsapp_name already exists in whatsapp_history and removes entries if it does
    cursor.execute('''
    DELETE FROM user_history WHERE whatsapp_name=?;
    ''', (whatsapp_name,))

    print(f"Session chats with whatsapp name {whatsapp_name} deleted from database.")
    conn.commit()
    cursor.close()
    conn.close()


def delete_existing_profile(whatsapp_name):
    conn = sqlite3.connect('/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM profiles WHERE whatsapp_name=?;
    ''', (whatsapp_name,))

    conn.commit()

    print(f"{whatsapp_name} profile deleted from database.")


    cursor.close()
    conn.close()

def insert_chats(whatsapp_name, whatsapp_history):
    chats = format_data(whatsapp_history) # get_all_message_objects(whatsapp_history)

    conn = sqlite3.connect(f'/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()

    # Delete existing chats 
    delete_existing_chats(whatsapp_name)

    # Insert chat objects into the database
    for chat in chats:
        insert_chat(conn, cursor, whatsapp_name, chat['date'], chat['time'], chat['name'], chat['message'])

    print(f"{len(chats)} {whatsapp_name} chats inserted into database.")
    cursor.close()
    conn.close()
    

# Function to insert a chat message into the database
def insert_chat(conn, cursor, whatsapp_name, date, time, name, message):
    cursor.execute(f'''
    INSERT INTO whatsapp_history (whatsapp_name, date, time, name, message) VALUES (?, ?, ?, ?, ?)
    ''', (whatsapp_name, date, time, name, message))
    conn.commit()

def show_table(cursor, table_name):
    # Execute a query to select all rows from the chats table
    cursor.execute(f'SELECT * FROM {table_name}')

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def show_tables(cursor):
    # Execute a query to select all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch all table names
    tables = cursor.fetchall()

    # Print the table names
    for table in tables:
        print(table[0])

def delete_table(table_name):
    if validate_table_name(table_name):
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        print(f"Table '{table_name}' deleted successfully.")

def initialize_database_tables():
    # Connect to SQLite database (creates the database if it doesn't exist)
    conn = sqlite3.connect(f'/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS whatsapp_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        whatsapp_name TEXT NOT NULL,
        date TEXT,
        time TEXT,
        name TEXT,
        message TEXT
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        whatsapp_name TEXT,
        message TEXT,
        speaker INT
    );
    ''')

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS profiles (
        whatsapp_name TEXT PRIMARY KEY,
        message_count INT,
        sentence_distribution TEXT,
        token_distribution TEXT,
        user_slang_dictionary TEXT,
        emoji_distribution TEXT,
        emoji_messages_examples TEXT,
        chunk TEXT
        
    );                       
    """)
    conn.commit()
    conn.close()

# comment out as needed, it is an executable environment
if __name__ == "__main__":

    whatsapp_name = "Valerie Suriato"

    conn = sqlite3.connect('/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()

    # delete_table('user_history') 
    # initialize_database_tables()   
    
    # insert_chats(whatsapp_name, "whatsapp_history", "/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/bryan.txt")

    delete_existing_profile(whatsapp_name)
    # show_tables(cursor)
    # show_table('whatsapp_history')
    # show_table('session_conversations')
    # show_table(cursor, 'user_history')
    conn.close()
