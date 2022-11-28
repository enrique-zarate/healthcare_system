import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS patients;')
cur.execute('''CREATE TABLE patients (id serial PRIMARY KEY,
                                        nombre VARCHAR(80) NOT NULL,
                                        fecha_nacimiento VARCHAR(80) NOT NULL, 
                                        signos_vitales VARCHAR(80) NOT NULL
                                        );''')


cur.execute('INSERT INTO patients (nombre, fecha_nacimiento, signos_vitales)'
            'VALUES (%s, %s, %s);', 
            ('Juan', '1990-01-01', '120/80')
            )


conn.commit()

cur.close()
conn.close()