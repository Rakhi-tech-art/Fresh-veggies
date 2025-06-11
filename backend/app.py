from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

DB_NAME = 'veg_prices.db'

# Initialize database if it doesn't exist
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vegetables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

# Get all veggie prices
@app.route('/get-prices', methods=['GET'])
def get_prices():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM vegetables")
    data = cursor.fetchall()
    conn.close()
    return jsonify([{ "name": name, "price": price } for name, price in data])

# Update price of a veggie
@app.route('/update-price', methods=['POST'])
def update_price():
    data = request.json
    name = data.get("name")
    price = data.get("price")

    if not name or price is None:
        return jsonify({"error": "Missing name or price"}), 400

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vegetables (name, price) VALUES (?, ?) ON CONFLICT(name) DO UPDATE SET price = excluded.price", (name, price))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Price updated for {name}", "price": price})

# Entry point
if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
