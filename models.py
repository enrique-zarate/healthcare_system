from flask_sqlalchemy import SQLAlchemy

# objeto de la base de datos
db = SQLAlchemy()

# crear un modelo paciente, con los datos de nombre, fecha de nacimiento, signos vitales
class Paciente(db.Model):

    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=False, nullable=False)
    fecha_nacimiento = db.Column(db.String(80), unique=False, nullable=False)
    signos_vitales = db.Column(db.String(80), unique=False, nullable=False)

    # constructor
    def __init__(self, id, nombre, fecha_nacimiento, signos_vitales):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.signos_vitales = signos_vitales

    # representacion del objeto
    def __repr__(self):
        return f'Paciente {self.nombre}'

