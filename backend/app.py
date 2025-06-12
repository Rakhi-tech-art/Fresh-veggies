from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

PRICES_FILE = os.path.join(os.path.dirname(__file__), 'prices.json')

# Load prices from JSON
def load_prices():
    with open(PRICES_FILE, 'r') as f:
        return json.load(f)

# Save prices to JSON
def save_prices(prices):
    with open(PRICES_FILE, 'w') as f:
        json.dump(prices, f, indent=2)

@app.route('/prices', methods=['GET'])
def get_prices():
    prices = load_prices()
    return jsonify([{"name": k, "price": v} for k, v in prices.items()])

@app.route('/update-price', methods=['POST'])
def update_price():
    data = request.json
    name = data.get("name")
    price = data.get("price")

    if not name or price is None:
        return jsonify({"error": "Missing name or price"}), 400

    prices = load_prices()
    prices[name] = price
    save_prices(prices)

    return jsonify({"message": f"Price for {name} updated to ₹{price}."}), 200

if __name__ == "__main__":
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))

