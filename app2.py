from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# ✅ Initialize the database
def init_db():
    conn = sqlite3.connect('users.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ⚠️ 1. SQL Injection Vulnerable Login
@app.route('/vulnerable_login', methods=['POST'])
def vulnerable_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # ⚠️ Vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("Executing:", query)
    result = cursor.execute(query).fetchone()
    conn.close()

    if result:
        return jsonify({"message": "Login Success (VULNERABLE to SQLi)"}), 200
    else:
        return jsonify({"message": "Invalid Credentials"}), 401

# ⚠️ 2. Registration with Plaintext Password (Unsafe Storage)
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        # ⚠️ Password stored as plain text
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return jsonify({"message": "User Registered (Password stored as-is)"}), 200
    except sqlite3.IntegrityError:
        return jsonify({"message": "User already exists"}), 409
    finally:
        conn.close()

# ⚠️ 3. XSS Vulnerable Endpoint
@app.route('/greet', methods=['POST'])
def greet_user():
    data = request.get_json()
    username = data.get("username")

    # ⚠️ Vulnerable to Cross-Site Scripting (XSS)
    return f"<h1>Hello {username}</h1>"

# ✅ 4. Safe Login with Parameterized Query
@app.route('/secure_login', methods=['POST'])
def secure_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify({"message": "Login successful (Safe)"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Run the app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)

