from flask import Flask
from models import db
from routes import usuarios_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ejercicio4.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secreto-ejercicio4'

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(usuarios_bp)

with app.app_context():
    db.create_all()

@app.route('/')
def inicio():
    return 'Servidor del Ejercicio 4 funcionando correctamente'

if __name__ == '__main__':
    app.run(debug=True)