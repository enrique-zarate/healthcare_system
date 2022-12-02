Proyecto de gestión de registros médicos

# How to run

## Linux

### Install packages

pip install -r requirements.txt

## Config the database

install postgres

create db

create user and set password

give permissions to user

### create tables and scheams

python3 init_db.py

### set user, password database enviroment variables for flask app

`export FLASK_APP=<python file name>`

### debug mode

`export FLASK_ENV=development`
`export FLASK_DEBUG=true`

### Run the server

`flask run`

### postgres engine

1. Check service status: `sudo service postgresql status`

2. Start service: `sudo service postgresql start`

3. Stop service if needed: `sudo service postgresql stop`

### run postgres in terminal

`sudo -u postgres psql`

### connect to db

`\c flask_db`
