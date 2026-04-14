from flask import Flask, request, jsonify
import subprocess
from datetime import datetime

app = Flask(__name__)

#  Define allowed commands
ALLOWED_COMMANDS = {
    "time": lambda: str(datetime.now()),
    "whoami": lambda: subprocess.getoutput("whoami"),
    "date": lambda: subprocess.getoutput("date")
}

@app.route("/")
def home():
    return " Flask - Safe Command Execution (No Injection!)"

@app.route("/execute", methods=["POST"])
def execute():
    data = request.get_json()
    command = data.get("code", "")

    if command in ALLOWED_COMMANDS:
        result = ALLOWED_COMMANDS[command]()  
    else:
        result = "Invalid or unsafe command"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
