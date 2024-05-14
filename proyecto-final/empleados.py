from flask import Blueprint, request, jsonify
from models import db
from models import Empleado

empleados_bp = Blueprint('empleados', __name__, url_prefix='/api/empleados')

@empleados_bp.route('/', methods=['POST'])
def crear_empleado():
    data = request.get_json()
    nuevo_empleado = Empleado(
        nombre=data['nombre'],
        email=data['email'],
        password=data['password']
    )
    db.session.add(nuevo_empleado)
    db.session.commit()
    return jsonify({'mensaje': 'Empleado creado exitosamente'}), 201

@empleados_bp.route('/<int:id>', methods=['GET'])
def obtener_empleado(id):
    # Buscar el empleado por su ID en la base de datos
    empleado = Empleado.query.get(id)

    # Verificar si se encontró el empleado
    if empleado:
        empleado_data = {
            'id': empleado.id,
            'nombre': empleado.nombre,
            'email': empleado.email,
        }
        return jsonify(empleado_data), 200
    else:
        # Si no se encuentra  devolver un mensaje de error
        return jsonify({'mensaje': 'Empleado no encontrado'}), 404

@empleados_bp.route('/<int:id>', methods=['PUT'])
def actualizar_empleado(id):
    # Obtener los datos del empleado desde la solicitud JSON
    data = request.get_json()

    # Buscar el empleado por su ID en la base de datos
    empleado = Empleado.query.get(id)

    # Verificar si se encontró el empleado
    if empleado:
        empleado.nombre = data.get('nombre', empleado.nombre)
        empleado.email = data.get('email', empleado.email)

        db.session.commit()

        return jsonify({'mensaje': 'Empleado actualizado exitosamente'}), 200
    else:
        # Si no se encuentra el empleado, devolver un mensaje de error
        return jsonify({'mensaje': 'Empleado no encontrado'}), 404
@empleados_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_empleado(id):
    empleado = Empleado.query.get(id)

    if empleado:
        # Eliminar el empleado de la base de datos
        db.session.delete(empleado)
        db.session.commit()

        return jsonify({'mensaje': 'Empleado eliminado exitosamente'}), 200
    else:
        return jsonify({'mensaje': 'Empleado no encontrado'}), 404
