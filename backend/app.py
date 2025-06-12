from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all domains (for development/testing)

# Route to get prices
@app.route('/prices', methods=['GET'])
def get_prices():
    # Example data; replace with your actual logic
    prices = [
        {"name": "Tomato", "price": 40},
        {"name": "Potato", "price": 30},
        {"name": "Onion", "price": 50}
    ]
    return jsonify(prices)

# Route to update a price
@app.route('/update-price', methods=['POST'])
def update_price():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')

    # Example logic to update price; replace with your actual logic
    print(f"Updating price for {name} to {price}")
    return jsonify({"message": f"Price for {name} updated to {price}."})

if __name__ == "__main__":
    app.run()