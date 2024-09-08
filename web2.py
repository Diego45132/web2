from flask import  Flask, render_template
import sqlite3
from pprint import pprint

# cargamos los datos 
conexion = sqlite3.connect('web2.sqlite3')
conexion.row_factory = sqlite3.Row # modo diccionario
cursor = conexion.cursor()
cursor.execute("""
SELECT * FROM productos;
""")
productos = [ dict(producto) for producto in cursor.fetchall() ]

cursor.close()
conexion.close()

# aplicacion
app = Flask(__name__)

# rutas 
@app.route('/')
def ruta_raiz():
  return render_template('index.html', productos=productos)

# programa principal
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)

