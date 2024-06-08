import sqlite3
from utils.parse import get_all_message_objects
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
    

def insert_chats(user_id, person_path):
    chats = get_all_message_objects(person_path)

    # Insert chat objects into the database
    for chat in chats:
        insert_chat(user_id, chat['date'], chat['time'], chat['name'], chat['message'])

# Function to insert a chat message into the database
def insert_chat(user_id, date, time, name, message):
    cursor.execute('''
    INSERT INTO conversations (user_id, date, time, name, message) VALUES (?, ?, ?, ?, ?)
    ''', (user_id, date, time, name, message))
    conn.commit()

def show_table(table_name):
    # Execute a query to select all rows from the chats table
    cursor.execute(f'SELECT * FROM {table_name}')

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def show_tables():
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
    # conn = sqlite3.connect(f'/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    # cursor = conn.cursor()

    # Create table for chunked conversations metadata
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS whatsapp_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        whatsapp_name TEXT NOT NULL,
        date TEXT,
        time TEXT,
        name TEXT,
        message TEXT
    )
    ''')


    # Create table for saving on-going conversation history
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS session_history (
        session_id TEXT PRIMARY KEY,
        message TEXT,
    );
    ''')


    cursor.execute("""
      CREATE TABLE IF NOT EXISTS profiles (
        session_id TEXT PRIMARY KEY,
        message TEXT, 
    );                       
    """)
    # conn.commit()
    # conn.close()

# comment out as needed, it is an executable environment
if __name__ == "__main__":

    whatsapp_name = "Bryan Widjaja"

    conn = sqlite3.connect('/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()

    delete_table('conversations')
    initialize_database_tables()  
    
    insert_chats(whatsapp_name, "/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/bryan.txt")

    show_tables()
    show_table('conversations')
    show_table('session_conversations')

    conn.close()
