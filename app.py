from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos (ajusta según tus credenciales)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'popo'
app.config['MYSQL_PASSWORD'] = 'popo'
app.config['MYSQL_DB'] = 'coco'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']

        # Insertar los datos en la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO form (nombre, apellido) VALUES (%s, %s)", (nombre, apellido))
        mysql.connection.commit()
        cursor.close()
        return 'Datos guardados exitosamente'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
