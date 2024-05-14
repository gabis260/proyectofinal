from flask import Blueprint, request, jsonify
from models import Empleado, db

from flask_sqlalchemy import SQLAlchemy



gestion_humana_bp = Blueprint('gestion_humana', __name__, url_prefix='/api/gestion_humana')

@gestion_humana_bp.route('/empleados', methods=['POST'])
def contratar_empleado():
    data = request.get_json()
    nuevo_empleado = Empleado(
        nombre=data['nombre'],
        email=data['email'],
        password=data['password'],
    )
    db.session.add(nuevo_empleado)
    db.session.commit()
    return jsonify({'mensaje': 'Empleado contratado exitosamente'}), 201

@gestion_humana_bp.route('/empleados/<int:id>', methods=['PUT'])
def actualizar_empleado(id):
    data = request.get_json()
    empleado = Empleado.query.get(id)
    if empleado:
        empleado.nombre = data.get('nombre', empleado.nombre)
        empleado.email = data.get('email', empleado.email)
        db.session.commit()
        return jsonify({'mensaje': 'Empleado actualizado exitosamente'}), 200
    else:
        return jsonify({'mensaje': 'Empleado no encontrado'}), 404

@gestion_humana_bp.route('/empleados/<int:id>', methods=['DELETE'])
def despedir_empleado(id):
    empleado = Empleado.query.get(id)
    if empleado:
        db.session.delete(empleado)
        db.session.commit()
        return jsonify({'mensaje': 'Empleado despedido exitosamente'}), 200
    else:
        return jsonify({'mensaje': 'Empleado no encontrado'}), 404