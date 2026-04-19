🔓 Vulnerable REST API (Security Testing Lab)

A deliberately insecure REST API built to demonstrate real-world web vulnerabilities and attack vectors.
This project allows developers and security enthusiasts to simulate attacks like SQL Injection, Broken Authentication, and Data Exposure in a controlled environment.

🚀 Features
Multiple vulnerable endpoints (Login, User Data, Admin Access)
SQL Injection simulation
Broken authentication & weak session handling
No input validation → exploit-ready APIs
Sensitive data exposure scenarios
Easily testable using Postman / Curl


🏗️ Tech Stack
Backend
Python (Flask) / Node.js (Express)
Database
SQLite / MySQL
Testing Tools
Postman
Burp Suite (optional)

User → API Request → Vulnerable Endpoint → Database Query (Unsafe) → Response (Exposed Data)

📦 API Overview

Endpoints include:

/login → vulnerable to SQL Injection
/users → exposes sensitive user data
/admin → weak authentication logic
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/vulnerable-api.git
cd vulnerable-api
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Server
python app.py
🔐 Vulnerability Demonstrations
SQL Injection
' OR '1'='1
Broken Authentication
Predictable session tokens
No rate limiting
🚧 Future Enhancements
Add secure version for comparison
JWT-based authentication
Input sanitization module
Rate limiting & logging
⚠️ Disclaimer

This project is intentionally insecure.
Do NOT deploy in production.

🏁 Conclusion

This project demonstrates how poorly designed APIs can be exploited and highlights the importance of secure coding practices.

🤝 Contributors

Srujana Reddy – Developer
