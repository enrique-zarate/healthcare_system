import os
import psycopg2
# importar dotenv
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'))

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS patients2;')
cur.execute('''CREATE TABLE patients2 (id serial PRIMARY KEY,
                                        nombre VARCHAR(80) NOT NULL,
                                        fecha_nacimiento VARCHAR(80) NOT NULL
                                        );''')


cur.execute('INSERT INTO patients2 (nombre, fecha_nacimiento)'
            'VALUES (%s, %s);', 
            ('Juan', '1990-01-01')
            )

# Execute a command: this creates a new table 'pressure_records' with a foreign key to 'patients'
cur.execute('DROP TABLE IF EXISTS pressure_records2;')
cur.execute('''CREATE TABLE pressure_records2(id serial PRIMARY KEY
                ,id_paciente INTEGER NOT NULL
                ,fecha_toma VARCHAR(80) NOT NULL
                ,signos_vitales VARCHAR(80) NOT NULL);''')

cur.execute('INSERT INTO pressure_records2 (id_paciente, fecha_toma, signos_vitales)'
                'VALUES (%s, %s, %s);',
                (1, '2020-01-01', '120/69')
                )

conn.commit()

cur.close()
conn.close()