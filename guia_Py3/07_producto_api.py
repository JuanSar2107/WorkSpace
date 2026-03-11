import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

class Producto:
    def __init__(self, nombre: str, precio: float):
        self._nombre = nombre
        self._precio = precio

    def get_datos(self):
        return {"nombre": self._nombre, "precio": self._precio}

class GestorProductos:
    def __init__(self):
        self.productos = []

    def agregar(self, nombre, precio):
        p = Producto(nombre, precio)
        self.productos.append(p)
        return p.get_datos()

app = Flask(__name__)
CORS(app)
gestor = GestorProductos()

@app.route('/api/productos', methods=['GET'])
def listar():
    return jsonify([p.get_datos() for p in gestor.productos]), 200

@app.route('/api/productos', methods=['POST'])
def crear():
    data = request.get_json()
    nuevo = gestor.agregar(data['nombre'], data['precio'])
    return jsonify({"mensaje": "Creado", "data": nuevo}), 201

if __name__ == '__main__':
    puerto = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=puerto, debug=True)