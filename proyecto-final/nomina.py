from flask import Blueprint, jsonify
from models import Nomina, Empleado, db
from datetime import datetime
from utils import calcular_salario, generar_desprendible
from correo import enviar_correo

nomina_bp = Blueprint('nomina', __name__, url_prefix='/api/nomina')

@nomina_bp.route('/<int:id>', methods=['GET'])
def obtener_nomina(id):
    empleado = Empleado.query.get(id)
    if empleado:
        nominas = Nomina.query.filter_by(empleado=empleado).all()
        nominas_data = [{'id': nomina.id, 'fecha': nomina.fecha.strftime('%Y-%m-%d'), 'salario': nomina.salario} for nomina in nominas]
        return jsonify(nominas_data), 200
    else:
        return jsonify({'mensaje': 'Empleado no encontrado'}), 404

@nomina_bp.route('/pago', methods=['POST'])

def pagar_nomina():
    empleados = Empleado.query.all()
    for empleado in empleados:
        # Calcular el salario del empleado
        salario = calcular_salario(empleado)

        # Generar el desprendible de pago en PDF
        desprendible_pdf = generar_desprendible(empleado, salario)

        nomina = Nomina(empleado=empleado, fecha=datetime.now(), salario=salario)
        db.session.add(nomina)
        db.session.commit()

        # Enviar la notificación por correo electrónico con el desprendible adjunto
        asunto = 'Desprendible de Pago'
        cuerpo = 'Se adjunta el desprendible de pago correspondiente.'
        enviar_correo(empleado.email, asunto, cuerpo, desprendible_pdf)
    return jsonify({'mensaje': 'Nómina pagada exitosamente'}), 200

