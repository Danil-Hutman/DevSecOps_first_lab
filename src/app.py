import os
import pymysql
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "cactus_store"),
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cactus")
def cactus_list():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cactus")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)