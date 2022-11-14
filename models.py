from flask_sqlalchemy import SQLAlchemy

# crear el modelo de la base de datos
db = SQLAlchemy()

# crear un modelo paciente, con los datos de nombre, fecha de nacimiento, signos vitales
class Paciente(db.Model):

    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=False, nullable=False)
    fecha_nacimiento = db.Column(db.String(80), unique=False, nullable=False)
    signos_vitales = db.Column(db.String(80), unique=False, nullable=False)

    # constructor
    def __init__(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.name}:{self.employee_id}"

