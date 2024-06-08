f

from utils.faiss_db import get_conversation_for_faiss
from utils.sqlite_db import create_db


def initialize_metadata_and_faiss(person_path, table_name):
    # Create a SQLite database and table
    conn, cursor = create_db("/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/conversations.db")
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        date TEXT,
        time TEXT,
        name TEXT,
        message TEXT
    )
    ''')
    conn.commit()

    conversations = get_conversation_for_faiss(person_path)

    # Insert the metadata into the database
    for i, message in enumerate(conversations):
        cursor.execute('''
        INSERT INTO conversations (id, date, time, name, message)
        VALUES (?, ?, ?, ?, ?)
        ''', (i, message['date'], message['time'], message['name'], message['message']))
    conn.commit()

    conn.close()


if __name__ == "__main__":
    pass