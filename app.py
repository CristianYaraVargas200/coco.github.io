from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'popo'
app.config['MYSQL_PASSWORD'] = 'popo'
app.config['MYSQL_DB'] = 'coco'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/POST', methods=['POST'])
def submit():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']

        # Inserta los datos en la base de datos
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO form (nombre, apellido) VALUES (%s, %s)", (nombre, apellido))
        mysql.connection.commit()
        cur.close()

        return 'Datos guardados exitosamente'

if __name__ == '__main__':
    app.run(debug=True)
