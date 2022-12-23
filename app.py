from flask import Flask, render_template, request, redirect, url_for
# import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# import pycopg2-binary
import psycopg2
# importar los modelos de la base de datos
from models import Paciente
from models import SignoVital
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
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
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
    patients = db.session.query(Paciente).all()
    # renderizar la plantilla
    return render_template('patients_list.html', patients=patients)

# endpoint to create a new patient
@app.route('/patients/new', methods=['GET', 'POST'])
def new_patient():
    if request.method == 'POST':
        print(request.form)
        # obtener los datos del formulario
        nombre = request.form['nombre']
        fecha_nacimiento = request.form['fecha_nacimiento']
        signos_vitales = request.form['signos_vitales']  # quitamos para que no se guarde en la tabla de pacientes, sino en la de registros
        # crear objeto Paciente
        paciente = Paciente(nombre, fecha_nacimiento)
        # insertar objeto paciente en la base de datos
        db.session.add(paciente)
        # guardar los cambios
        db.session.commit()
        # insertar entrada en la tabla de registros
        # seleccionar el campo 'id' del ultimo paciente de la tabla pacientes
        paciente_q = db.session.query(Paciente).order_by(Paciente.id.desc()).first()
        # crear objeto SignoVital con el id del paciente creado en la linea anterior
        signo_vital = SignoVital(paciente_q.id, '2020-01-01', signos_vitales)
        
        # insertar objeto signo vital en la base de datos
        db.session.add(signo_vital)
        # guardar los cambios
        db.session.commit()
        return redirect(url_for('patients'))
    
    return render_template('new_patient.html')

# endpoint to edit a patient
@app.route('/patients/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    # get data from html form
    if request.method == 'POST':
        # get data from html form
        nombre = request.form['nombre']
        fecha_nacimiento = request.form['fecha_nacimiento']
        # signos_vitales = request.form['signos_vitales']
        # create a connection to the database and the user data
        patient = db.session.query(Paciente).filter_by(id=id).first()
        patient.nombre = nombre
        patient.fecha_nacimiento = fecha_nacimiento
        # patient.signos_vitales = signos_vitales
        db.session.commit()
        return redirect(url_for('patients'))
    return render_template('patient.html', patient=db.session.query(Paciente).get(id))

# endpoint for adding a new registry to the patient
@app.route('/patients/<id>/signos_vitales/new', methods=['GET', 'POST'])
def new_signos_vitales(id):
    if request.method == 'POST':
        # get data from html form
        id_paciente = id
        signos_vitales = request.form['signo_vital']
        fecha_toma = request.form['fecha_toma']
        # create a connection to the database and the user data
        vital_signs = SignoVital(id_paciente, fecha_toma, signos_vitales)
        db.session.add(vital_signs)
        db.session.commit()
        return redirect(url_for('new_signos_vitales', id=id))
    return render_template('signos_vitales.html', signos_vitales=db.session.query(SignoVital).filter_by(id_paciente=id).all())

# endpoint to search a patient
@app.route('/patients/search', methods=['GET', 'POST'])
def search_patient():
    if request.method == 'POST':
        # obtener id del form
        id = request.form['id']
        print(id)
        patients = db.session.query(Paciente).filter_by(id=id).all()
        return render_template('patients_list.html', patients=patients)


# endpoint to delete a patient
@app.route('/patients/delete/<int:id>')
def delete_patient(id):
    patient = db.session.query(Paciente).filter_by(id=id).first()
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('patients'))


if __name__ == '__main__':
    app.run(debug=True)