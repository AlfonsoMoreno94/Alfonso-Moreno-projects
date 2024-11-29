# Buscar canciones en el cancionero

    # Cargar base de datos

from flask import Flask, render_template
import mysql.connector
app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rootroot',
        database='cancionero'
    )
    return connection

connection = get_db_connection()
db = connection.cursor(dictionary=True)

@app.route('/')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
