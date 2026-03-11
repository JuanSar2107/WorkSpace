import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

@app.route('/api/config', methods=['GET'])
def obtener_config():
    ambiente = os.getenv("FLASK_ENV", "Producción")
    return jsonify({"status": "Servidor seguro", "entorno": ambiente}), 200

if __name__ == '__main__':
    puerto = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=puerto, debug=True)
    