Vulnerable REST API (Security Testing Project)
📌 Overview

This project is a deliberately insecure REST API designed to demonstrate common web vulnerabilities and how attackers exploit them. Think of it as a controlled environment where you can simulate real-world attacks like SQL Injection, Broken Authentication, and Insecure Data Exposure.

Instead of just learning theory, this project forces you to see how APIs break under poor security practices.

⚙️ How It Works

The API is built using a backend framework (Flask/Node.js depending on your implementation) and exposes multiple endpoints such as login, user data retrieval, and data submission.

Each endpoint is intentionally designed with flaws:

SQL Injection → Input fields directly passed into queries without sanitization
Broken Authentication → Weak session/token handling
No Rate Limiting → Allows brute-force attacks
Sensitive Data Exposure → Returns raw data without masking

When a user interacts with the API:

Request hits endpoint
No validation/sanitization occurs
Database query executes directly
Vulnerability can be exploited

🧠 Key Learning Areas
OWASP Top 10 vulnerabilities
API security flaws in real systems
Attack simulation techniques
Secure coding practices (when fixed version is implemented)

🛠️ Tech Stack
Backend: Python (Flask) / Node.js (Express)
Database: SQLite / MySQL
Tools: Postman / Curl
Security Testing: Burp Suite (optional)

🚀 Features
Multiple vulnerable endpoints
Real-world attack scenarios
Easy testing using Postman
Extendable for adding more vulnerabilities

▶️ How to Run
git clone <repo>
cd vulnerable-api
pip install -r requirements.txt
python app.py

Test endpoints using Postman.

⚠️ Important

This project is intentionally insecure.
Do NOT deploy it publicly.
