from flask import Flask, jsonify
from flask_cors import CORS
import sqlitecloud
import os

# Crear la aplicación Flask
app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde diferentes dominios (CORS)

# Conexión a SQLite Cloud
conn = sqlitecloud.connect("sqlitecloud://cpxoojbnnk.sqlite.cloud:8860?apikey=KlWlcnawgXjsKrwLiBIGsDIsv0NE07BaI9TE7cmoGLc")
conn.execute("USE DATABASE inventario.db")

# Endpoint para obtener datos del inventario
@app.route('/piezas', methods=['GET'])
def get_piezas():
    try:
        cursor = conn.execute("SELECT id, nombre, cantidad, foto FROM piezas")
        piezas = cursor.fetchall()

        # Convertir los datos en una lista de diccionarios
        data = [
            {"id": row[0], "nombre": row[1], "cantidad": row[2], "foto": row[3]}
            for row in piezas
        ]
        return jsonify(data), 200  # Responder con JSON y código HTTP 200 (OK)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Responder con error 500 en caso de fallo


# Ejecutar el servidor solo si este archivo se ejecuta directamente
if __name__ == '__main__':
    puerto = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=puerto, debug=True)

