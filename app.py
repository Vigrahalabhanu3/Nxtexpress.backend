from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

products = [
  {
    "id": 1,
    "name": "Chopping Board",
    "price": 360,
    "description": "A durable wooden chopping board for daily kitchen use.",
    "image": "https://bit.ly/3XCmlH5"
  },
  {
    "id": 2,
    "name": "Sketch Pens",
    "price": 30,
    "description": "12 bright colors perfect for school and art projects.",
    "image": "https://bit.ly/3X8Tb2d"
  },
  {
    "id": 3,
    "name": "Shoes",
    "price": 519,
    "description": "Comfortable running shoes with breathable mesh.",
    "image": "https://bit.ly/4r5FnTX"
  },
  {
    "id": 4,
    "name": "Water Bottle",
    "price": 199,
    "description": "1-litre stainless steel insulated bottle.",
    "image": "https://bit.ly/48oQWy3"
  },
  {
    "id": 5,
    "name": "Notebook",
    "price": 85,
    "description": "200-page ruled notebook for study & office use.",
    "image": "https://images.unsplash.com/photo-1519682337058-a94d519337bc"
  },
  {
    "id": 6,
    "name": "Earphones",
    "price": 299,
    "description": "High-quality wired earphones with mic.",
    "image": "https://bit.ly/4i705i2"
  },
  {
    "id": 7,
    "name": "Backpack",
    "price": 899,
    "description": "Lightweight waterproof backpack with 3 compartments.",
    "image": "https://bit.ly/4ocvZuZ"
  },
  {
    "id": 8,
    "name": "LED Bulb",
    "price": 120,
    "description": "9W energy-efficient LED bulb.",
    "image": "https://bit.ly/49oKyI9"
  },
  {
    "id": 9,
    "name": "Coffee Mug",
    "price": 250,
    "description": "Ceramic mug with heat insulation and stylish print.",
    "image": "https://bit.ly/48uDdov"
  },
  {
    "id": 10,
    "name": "Keyboard",
    "price": 750,
    "description": "USB keyboard with smooth keys and long durability.",
    "image": "https://bit.ly/3X6DtEU"
  }
]



@app.route('/products')
def product_list():
  return jsonify(products)


if __name__ == '__main__':
  # Read PORT and debug settings from environment for local development.
  # In production, run using a WSGI server like gunicorn (Procfile/Dockerfile provided).
  port = int(os.environ.get('PORT', 5001))
  debug = os.environ.get('FLASK_DEBUG', '0') == '1'
  app.run(host='0.0.0.0', port=port, debug=debug)