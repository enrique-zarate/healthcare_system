from flask_sqlalchemy import SQLAlchemy

# crear el modelo de la base de datos
db = SQLAlchemy()

# crear un modelo paciente
class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable)

    # crear el constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # crear el metodo para representar el objeto
    def __repr__(self):
        return '<Patient %r>' % self.name
