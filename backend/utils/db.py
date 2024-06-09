import sqlite3
from datetime import datetime

# Example chat objects
chats = [
    {'role': 'system', 'content': "Yo what's up bro?"},
    {'role': 'user', 'content': "remember last time we talked about airplanes, tell me how those work"}
]


# Function to insert a chat message into the database
def insert_chat(sender, content):
    cursor.execute('''
        INSERT INTO chats (sender, content) VALUES (?, ?)
    ''', (sender, content))
    conn.commit()


def create_table():

    # Create a table to store chat messages
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()


def insert_chats():
    # Insert chat objects into the database
    for chat in chats:
        insert_chat(chat['role'], chat['content'])


def show_chat_db():
    # Execute a query to select all rows from the chats table
    cursor.execute('SELECT * FROM chats')

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print the fetched rows
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


if __name__ == "__main__":
    # Connect to SQLite database (creates the database if it doesn't exist)
    conn = sqlite3.connect('chat.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Insert function commands here
    show_chat_db()

    # Close the connection
    conn.close()
