import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
''')

conn.commit()
conn.close()

print("Database and table created successfully!")