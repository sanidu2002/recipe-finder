from flask import Flask, render_template, request, jsonify
import requests
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS favorites(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        instructions TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    ingredient = request.args.get("ingredient")

    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"

    response = requests.get(url)
    data = response.json()

    return jsonify(data)

@app.route("/favorite", methods=["POST"])
def favorite():

    data = request.json

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute(
        "INSERT INTO favorites (name,instructions) VALUES (?,?)",
        (data["name"], data["instructions"])
    )

    conn.commit()
    conn.close()

    return {"message":"saved"}

@app.route("/favorites")
def show_favorites():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT name FROM favorites")

    favorites = c.fetchall()

    conn.close()

    return jsonify(favorites)

if __name__ == "__main__":
    app.run(debug=True)