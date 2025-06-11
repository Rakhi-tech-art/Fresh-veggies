from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

PRICES_FILE = os.path.join(os.path.dirname(__file__), 'prices.json')

def load_prices():
    with open(PRICES_FILE, 'r') as f:
        return json.load(f)

def save_prices(prices):
    with open(PRICES_FILE, 'w') as f:
        json.dump(prices, f, indent=2)

@app.route("/prices", methods=["GET"])
def get_prices():
    try:
        prices = load_prices()
        return jsonify(prices)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/update_price", methods=["POST"])
def update_price():
    try:
        data = request.get_json()
        name = data.get("name")
        price = data.get("price")

        prices = load_prices()
        prices[name] = price
        save_prices(prices)

        return jsonify({"message": "Price updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
