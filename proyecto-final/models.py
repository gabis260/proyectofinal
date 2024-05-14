from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

class Gestion_humana(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)

class Nomina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)
    empleado = db.relationship('Empleado', backref=db.backref('nominas', lazy=True))
    fecha = db.Column(db.Date, nullable=False)
    salario = db.Column(db.Float, nullable=False)
