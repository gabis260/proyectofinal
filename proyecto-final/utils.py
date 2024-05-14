import pdfkit  # Librería para generar PDFs desde HTML
import smtplib  # Librería para enviar correos electrónicos
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def calcular_salario(empleado):
    # Salario base
    salario_base = 1000000

    # Descuentos
    descuento_salud = salario_base * 0.04  # 4% de descuento para salud
    descuento_pension = salario_base * 0.04  # 4% de descuento para pensión

    # Cálculo del salario neto
    salario_neto = salario_base - descuento_salud - descuento_pension

    return salario_neto
def generar_desprendible(empleado, salario):
    html = f"""
    <html>
    <body>
        <h1>Desprendible de Pago</h1>
        <p>Empleado: {empleado.nombre}</p>
        <p>Salario: {salario} COP</p>
        <!-- Agrega más detalles según tus necesidades -->
    </body>
    </html>
    """

    # Convierte el HTML a PDF utilizando pdfkit
    opciones = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8"
    }
    desprendible_pdf = pdfkit.from_string(html, False, options=opciones)

    return desprendible_pdf




def generar_desprendible(empleado, salario):
    # Genera el HTML con los detalles del desprendible
    html = f"""
    <html>
    <body>
        <h1>Desprendible de Pago</h1>
        <p>Empleado: {empleado.nombre}</p>
        <p>Salario: {salario} COP</p>
        <!-- Agrega más detalles según tus necesidades -->
    </body>
    </html>
    """

    # Convierte el HTML a PDF utilizando pdfkit
    opciones = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8"
    }
    desprendible_pdf = pdfkit.from_string(html, False, options=opciones)

    return desprendible_pdf