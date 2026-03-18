from flask import Blueprint, request, jsonify
from models import db, Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()

    if not data or not data.get('nombre') or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    usuario_existente = Usuario.query.filter_by(email=data['email']).first()
    if usuario_existente:
        return jsonify({'error': 'El correo ya está registrado'}), 400

    password_hash = generate_password_hash(data['password'])

    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        email=data['email'],
        password=password_hash
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'mensaje': 'Usuario registrado correctamente'}), 201


@usuarios_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Faltan credenciales'}), 400

    usuario = Usuario.query.filter_by(email=data['email']).first()

    if not usuario or not check_password_hash(usuario.password, data['password']):
        return jsonify({'error': 'Credenciales inválidas'}), 401

    token = create_access_token(identity=str(usuario.id))

    return jsonify({
        'mensaje': 'Login exitoso',
        'token': token
    }), 200


@usuarios_bp.route('/perfil', methods=['GET'])
@jwt_required()
def perfil():
    usuario_id = get_jwt_identity()
    usuario = Usuario.query.get(usuario_id)

    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    return jsonify({
        'id': usuario.id,
        'nombre': usuario.nombre,
        'email': usuario.email
    }), 200