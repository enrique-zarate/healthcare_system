from flask import Flask, render_template, request, redirect, url_for
# import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# import pycopg2-binary
import psycopg2
# importar los modelos de la base de datos
from models import Paciente
# import os
import os


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

# create object connection
conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
        


# # crear una conexion a la base de datos postgres
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask_db'
# # desactivar el track de modificaciones
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # inicializar la base de datos
# db.init_app(app)

# def connection():
#     s = 'localhost:5432/flask_db' #Your server(host) name 
#     d = 'patients' #Your database name
#     u = 'enri' #Your login user
#     p = 'kike2311' #Your login password
#     conn = psycopg2.connect(host=s, user=u, password=p, database=d)
#     return conn
    
# conn = connection()



# # create postgres tables
# @app.before_first_request
# def create_tables():
#     db.create_all()

@app.route('/')
def index():
    return {'Saludo' : 'Hola Mundo'}



# crear ruta para mostrar los pacientes
@app.route('/patients')
def patients():
    # create a connection to the database and the user data
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
    # crear una lista de pacientes
    patients = []
    # crear conexion a la base de datos y los datos del usuario
    # conn = psycopg2.connect("dbname=flask_db user=enri")
    # crear cursor
    cur = conn.cursor()
    # ejecutar query
    cur.execute("SELECT * FROM patients")
    # fetch de los datos a la tabla
    for row in cur.fetchall():
        patients.append({"id": row[0], "nombre": row[1], "fecha_nacimiento": row[2], "signos_vitales": row[3]})
    conn.close()
    return render_template('patients_list.html', patients=patients)

    # create an endpoint to edit a patient
@app.route('/patients/<int:id>' , methods=['GET', 'POST'])
def patient(id):
    # create a connection to the database and the user data
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
    # create a cursor
    cur = conn.cursor()
    # execute query
    cur.execute("SELECT * FROM patients WHERE id=%s", (id,))
    # fetch the data from the table
    row = cur.fetchone()
    # print(row)
    conn.close()
    return render_template('patient.html', patient=row)

# endpoint to create a new patient
@app.route('/patients/new', methods=['GET', 'POST'])
def new_patient():
    # create a connection to the database and the user data
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

    # obtener los datos del formulario
    print(request.form)
    nombre = request.form['nombre']
    fecha_nacimiento = request.form['fecha_nacimiento']
    signos_vitales = request.form['signos_vitales']
    
    # create a cursor
    cur = conn.cursor()
    # query de insercion de datos
    cur.execute("INSERT INTO patients (nombre, fecha_nacimiento, signos_vitales) VALUES (%s, %s, %s)",
                                      (nombre, fecha_nacimiento, signos_vitales))
    conn.commit()
    conn.close()
    return render_template('new_patient.html')
