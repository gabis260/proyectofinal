from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from models import db
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nomina.db'
db.init_app(app)
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Sistema de Nómina'
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# Crear las tablas de la base de datos
with app.app_context():
    db.create_all()

from empleados import empleados_bp
from nomina import nomina_bp
from gestion_humana import gestion_humana_bp

app.register_blueprint(empleados_bp)
app.register_blueprint(nomina_bp)
app.register_blueprint(gestion_humana_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/empleados')
def empleados():
    return render_template('empleados.html')

@app.route('/nomina')
def nomina():
    return render_template('nomina.html')

@app.route('/gestion-humana')
def gestion_humana():
    return render_template('gestion_humana.html')

if __name__ == '__main__':
    app.run(debug=True)