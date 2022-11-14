from flask import Flask
# import templating engine
from flask import render_template

app = Flask(__name__)

# crear una conexion a la base de datos postgres
# postgresql://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask'

@app.route('/')
def index():
    return render_template('index.html')