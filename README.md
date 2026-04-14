This project is designed to simulate real-world web application vulnerabilities based on common security flaws found in modern APIs. It acts as a controlled environment to understand how attacks work and how to fix them.

The system is built using Python and Flask, where multiple API endpoints are intentionally developed with insecure coding practices. These endpoints replicate vulnerabilities such as SQL Injection, Cross-Site Scripting (XSS), Insecure Direct Object Reference (IDOR), and Command Injection.

Each vulnerability is tested using Postman by sending crafted inputs to exploit the weaknesses. For example, SQL Injection is demonstrated using unsanitized queries, while XSS is triggered through unescaped user inputs. Command Injection is performed using unsafe execution methods.

After identifying these vulnerabilities, the project implements proper security fixes including input validation, parameterized queries, and strict authorization controls. This helps demonstrate both the attack and defense sides of cybersecurity.

Overall, the project provides hands-on experience with OWASP Top 10 vulnerabilities, making it useful for understanding real-world API security risks and mitigation strategies.
