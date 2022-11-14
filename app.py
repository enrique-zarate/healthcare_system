from flask import Flask
# import libraries
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
# import pycopg2-binary
import psycopg2
# importar los modelos de la base de datos
from models import Paciente

# crear la aplicacion
app = Flask(__name__)

# creamos objeto de base de datos
db = SQLAlchemy(app)

# # crear una conexion a la base de datos postgres
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask_db'
# # desactivar el track de modificaciones
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # inicializar la base de datos
# db.init_app(app)

def connection():
    s = 'localhost:5432/flask_db' #Your server(host) name 
    d = 'patients' #Your database name
    u = 'enri' #Your login user
    p = 'kike2311' #Your login password
    conn = psycopg2.connect(host=s, user=u, password=p, database=d)
    return conn
    
conn = connection()


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
    # crear una lista de pacientes
    patients = []
    # crear conexion a la base de datos y los datos del usuario
    conn = psycopg2.connect("dbname=flask_db user=enri")
    # crear cursor
    cur = conn.cursor()
    # ejecutar query
    cur.execute("SELECT * FROM patients")
    # fetch de los datos a la tabla
    for row in cur.fetchall():
        patients.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
    conn.close()
    return render_template('patients.html', patients=patients)