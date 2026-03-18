import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///default.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'clave-insegura')

@app.route('/')
def inicio():
    return {"mensaje": "Fase 1 funcionando correctamente"}

if __name__ == '__main__':
    puerto = int(os.getenv('PORT', 5000))
    modo_debug = os.getenv('FLASK_DEBUG') == 'True'
    app.run(port=puerto, debug=modo_debug)