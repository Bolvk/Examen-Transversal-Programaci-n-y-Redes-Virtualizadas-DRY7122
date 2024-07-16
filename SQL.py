from flask import Flask, request
import sqlite3
from bcrypt import hashpw, gensalt, checkpw

app = Flask(__name__)
DATABASE = 'usuarios.db'

def reset_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS usuarios''')
    conn.commit()
    conn.close()

def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

def insert_user(username, password):
    hashed_password = hashpw(password.encode('utf-8'), gensalt())
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE username=?", (username,))
    user = c.fetchone()
    if not user:
        c.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print(f"User {username} inserted.")
    else:
        print(f"User {username} already exists.")
    conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT password FROM usuarios WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    if user and checkpw(password.encode('utf-8'), user[0]):
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            return 'Inicio de sesión exitoso'
        else:
            return 'Credenciales incorrectas'
    else:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Autenticación de Usuario</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f2f2f2;
                }
                .container {
                    width: 400px;
                    margin: 100px auto 0 auto;
                    padding: 20px 40px;
                    background-color: white;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    text-align: center;
                }
                form {
                    margin-top: 20px;
                }
                label {
                    display: block;
                    margin-bottom: 10px.
                }
                input[type="text"],
                input[type="password"] {
                    width: 100%;
                    padding: 10px.
                    margin-bottom: 15px.
                    border: 1px solid #ccc.
                    border-radius: 5px.
                }
                input[type="submit"] {
                    width: 100%.
                    padding: 10px.
                    background-color: #007bff.
                    border: none.
                    border-radius: 5px.
                    color: white.
                    font-size: 16px.
                    cursor: pointer.
                }
                input[type="submit"]:hover {
                    background-color: #0056b3.
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Autenticación de Usuario</h1>
                <form action="/" method="post">
                    <label for="username">Nombre de Usuario:</label>
                    <input type="text" id="username" name="username" autocomplete="off">
                    <label for="password">Contraseña:</label>
                    <input type="password" id="password" name="password" autocomplete="off">
                    <input type="submit" value="Iniciar Sesión">
                </form>
            </div>
        </body>
        </html>
        '''

if __name__ == '__main__':
    reset_table()
    create_table()
    # Insertar usuarios (nombre de los integrantes del examen y contraseñas a elección)
    insert_user('adelmoral', 'duoc2024')
    insert_user('nombre2', 'contrasena2')
    insert_user('nombre3', 'contrasena3')
    # Ejecutar la aplicación en el puerto 5800
    app.run(port=5800)
