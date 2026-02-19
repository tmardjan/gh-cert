import sqlite3
import os
from flask import Flask, request

app = Flask(__name__)

# 🚨 Hardcoded secret (CodeQL should flag this)
API_KEY = "ghp_1234567890FAKEHARDCODEDSECRET"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # 🚨 SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return result

@app.route("/user")
def user_lookup():
    username = request.args.get("username")
    return str(get_user(username))

@app.route("/ping")
def ping():
    host = request.args.get("host")

    # 🚨 Command Injection vulnerability
    os.system("ping -c 1 " + host)

    return "Ping executed"

if __name__ == "__main__":
    app.run(debug=True)
