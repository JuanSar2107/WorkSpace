from flask import Blueprint, request, jsonify
from models import db, Usuario

usuarios_bp = Blueprint('usuarios', __name__)

# Crear usuario
@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()

    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        email=data['email']
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'mensaje': 'Usuario creado correctamente'}), 201

# Obtener todos los usuarios
@usuarios_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()

    resultado = []
    for usuario in usuarios:
        resultado.append({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'email': usuario.email
        })

    return jsonify(resultado)

# Obtener un usuario por ID
@usuarios_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get_or_404(id)

    return jsonify({
        'id': usuario.id,
        'nombre': usuario.nombre,
        'email': usuario.email
    })

# Actualizar usuario
@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json()

    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.email = data.get('email', usuario.email)

    db.session.commit()

    return jsonify({'mensaje': 'Usuario actualizado correctamente'})

# Eliminar usuario
@usuarios_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({'mensaje': 'Usuario eliminado correctamente'})