from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv


db = SQLAlchemy()


# crear un modelo paciente, con los datos de nombre, fecha de nacimiento, signos vitales
class Paciente(db.Model):

    __tablename__ = "patients2"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=False, nullable=False)
    fecha_nacimiento = db.Column(db.String(80), unique=False, nullable=False)
    # signos_vitales = db.Column(db.String(80), unique=False, nullable=False) se guarda en la tabla de registros

    # constructor
    def __init__(self, nombre, fecha_nacimiento):
        # self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        # self.signos_vitales = signos_vitalesd

    # representacion del objeto
    def __repr__(self):
        return f'Paciente {self.id}'


# crear una clase registro de presiones, con los datos de id de paciente, fecha de la toma, y signos vitales
class SignoVital(db.Model):
    
        __tablename__ = "pressure_records2"
    
        id = db.Column(db.Integer, primary_key=True)
        id_paciente = db.Column(db.Integer, unique=False, nullable=False)
        fecha_toma = db.Column(db.String(80), unique=False, nullable=False)
        signos_vitales = db.Column(db.String(80), unique=False, nullable=False)
    
        # constructor
        def __init__(self, id_paciente, fecha_toma, signos_vitales):
            self.id_paciente = id_paciente
            self.fecha_toma = fecha_toma
            self.signos_vitales = signos_vitales
    
        # representacion del objeto
        def __repr__(self):
            return f'Registro de presion {self.id}'



# db.create_all()