from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home page
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        conn = get_db_connection()

        conn.execute(
            'INSERT INTO users (name, email) VALUES (?, ?)',
            (name, email)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    conn = get_db_connection()

    users = conn.execute(
        'SELECT * FROM users'
    ).fetchall()

    conn.close()

    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)

import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

conn.commit()
conn.close()
