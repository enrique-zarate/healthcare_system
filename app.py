from flask import Flask, render_template, request
# import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# import pycopg2-binary
import psycopg2
# importar los modelos de la base de datos
from models import Paciente
# import os
import os
# importar dotenv
from dotenv import load_dotenv
# cargar las variables de entorno
load_dotenv()

# crear la aplicacion
app = Flask(__name__)

# creamos objeto de base de datos

# configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://enri:kike2311@localhost:5432/flask_db'
# desactivar el track de modificaciones
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# inicializar la base de datos
db = SQLAlchemy(app)
db.init_app(app)

@app.route('/')
def index():
    return '<h2>Hola Mundo</h2>'

# crear ruta para mostrar los pacientes
@app.route('/patients')
def patients():
    # obtener los pacientes de la base de datos
    pacientes = Paciente.query.all()
    # renderizar la plantilla
    return render_template('patients.html', pacientes=pacientes)

# create an endpoint to edit a patient
@app.route('/patients/<int:id>' , methods=['GET', 'POST'])
def patient(id):
    # get data from html form
    if request.method == 'POST':
        # get data from html form
        name = request.form['name']
        birth_date = request.form['birth_date']
        vital_signs = request.form['vital_signs']
        # create a connection to the database and the user data
        paciente = Paciente.query.get(id)
        paciente.name = name
        paciente.birth_date = birth_date
        paciente.vital_signs = vital_signs
        db.session.commit()
        return render_template('patient.html', patient=paciente)
    return render_template('patient.html', patient=Paciente.query.get(id))

# endpoint to create a new patient
@app.route('/patients/new', methods=['GET', 'POST'])
def new_patient():
    if request.method == 'POST':
        print(request.form)
        # obtener los datos del formulario
        nombre = request.form['nombre']
        fecha_nacimiento = request.form['fecha_nacimiento']
        signos_vitales = request.form['signos_vitales']
        # crear objeto Paciente
        paciente = Paciente(nombre, fecha_nacimiento, signos_vitales)
        # insertar objeto paciente en la base de datos
        db.session.add(paciente)
        # guardar los cambios
        db.session.commit()

        return 'Paciente creado'
    
    return render_template('new_patient.html')

# endpoint to edit a patient
@app.route('/patients/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    db.session.query(Paciente).filter(Paciente.id == id).update(request.form)
    db.session.commit()
    return 'Paciente actualizado'

# endpoint to search a patient
@app.route('/patients/search/<string:name>')
def search_patient(name):
    # obtener el paciente de la base de datos
    paciente = Paciente.query.filter_by(name=name).first()
    # renderizar la plantilla
    return render_template('patient.html', patient=paciente)