from flask import Flask, request
import sqlite3

app = Flask(__name__)
# 1-Muammo: Maxfiy kalit ochiq matn ko'rinishida (Bandit buni aniqlaydi)
app.secret_key = "SUPER_SECRET_COMPROMISED_KEY"

@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # 2-Muammo: SQL Injection zaifligi (Bandit buni ham aniqlaydi)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    return str(cursor.fetchall())

if __name__ == '__main__':
    app.run(debug=True)

