from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# PostgreSQL Connection
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_NAME = os.getenv("DB_NAME", "arafat_database")
DB_USER = os.getenv("DB_USER", "test")
DB_PASS = os.getenv("DB_PASS", "test")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    print(users)

    return jsonify([{"name": u[0]} for u in users])

if __name__ == '__main__':
    app.run(debug=True)
