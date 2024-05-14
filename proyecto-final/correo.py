import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def enviar_correo(destinatario, asunto, cuerpo, adjunto=None):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'gabigon2604@gmail.com'
    smtp_password = 'Jhnsjb260'

    mensaje = MIMEMultipart()
    mensaje['From'] = smtp_username
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    if adjunto:
        archivo = MIMEApplication(adjunto.read(), _subtype='pdf')
        archivo.add_header('Content-Disposition', 'attachment', filename='desprendible.pdf')
        mensaje.attach(archivo)

    with smtplib.SMTP(smtp_server, smtp_port) as servidor:
        servidor.starttls()
        servidor.login(smtp_username, smtp_password)
        servidor.send_message(mensaje)