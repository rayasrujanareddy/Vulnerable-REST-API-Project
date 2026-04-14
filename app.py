from flask import Flask, request, jsonify
import sqlite3
import uuid
import os

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

# 🔥 One endpoint for all vulnerabilities
@app.route('/test_all_vulnerabilities', methods=['POST'])
def test_all_vulnerabilities():
    data = request.get_json()

    username = data.get("username", "")
    password = data.get("password", "")
    expression = data.get("expression", "")
    user_id = data.get("user_id", 1)

    output = {}

    # 1. SQL Injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    vulnerable_query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("SQL Injection Test Query:", vulnerable_query)
    result = cursor.execute(vulnerable_query).fetchone()
    output['sql_injection'] = "Success" if result else "Failed"

    # 2. Plaintext Password Registration
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        output['plaintext_password_storage'] = "User registered"
    except sqlite3.IntegrityError:
        output['plaintext_password_storage'] = "User already exists"

    # 3. XSS
    output['xss'] = f"<h1>Hello {username}</h1>"

    # 4. Secure Login Check
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    secure_result = cursor.fetchone()
    output['secure_login'] = "Success" if secure_result else "Failed"

    # 5. Broken Authentication (Predictable Token)
    token = username + "123"
    output['predictable_token'] = token

    # 6. Brute-force Simulation (No Rate Limiting)
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    brute_result = cursor.fetchone()
    output['brute_force'] = "Success" if brute_result else "Failed"

    # 7. Insecure Direct Object Reference (IDOR)
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()
    if user:
        output['idor'] = {"id": user[0], "username": user[1], "password": user[2]}
    else:
        output['idor'] = "User not found"

    conn.close()

    # 8. Command Injection (eval)
    try:
        eval_result = eval(expression)
        output['command_injection'] = eval_result
    except Exception as e:
        output['command_injection'] = f"Error: {str(e)}"

    return jsonify(output)

# ✅ Run the app (Debug mode ON = ⚠️ Security Misconfiguration)
if __name__ == '__main__':
    init_db()
    app.run(debug=True) 