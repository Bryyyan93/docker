from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
import logging
import sys
import time
from sqlalchemy.exc import OperationalError


app = Flask(__name__)

# Cargar la configuración desde el archivo config.py
app.config.from_object(Config)

# Configuración de los logs en formato JSON
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()

#  Permite que la aplicación interactúe con la base de datos
db = SQLAlchemy(app)

# Variables para controlar el estado
is_healthy = True
is_ready = True

# Modelo de la base de datos
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Note {self.title}>'
    
# Ruta para liveness probe
@app.route('/health', methods=['GET'])
def health():
    # Si está todo correcto, retornamos un código 200.
    if is_healthy:
        return jsonify({"status": "healthy"}), 200
    else:
        return jsonify({"status": "unhealthy"}), 500 # Simular fallo

# Ruta para readiness probe
@app.route('/ready', methods=['GET'])
def ready():
    # Aquí puedes verificar si la app está lista para recibir tráfico.
    # Si todo está correcto, retornamos un código 200.
    if is_ready:
        return jsonify({"status": "ready"}), 200
    else:
        return jsonify({"status": "unready"}), 500

# Endpoint para cambiar el estado de health y readiness manualmente (pruebas)

@app.route('/set_health/<status>', methods=['POST'])
def set_health(status):
    global is_healthy
    if status == 'healthy':
        is_healthy = True
    elif status == 'unhealthy':
        is_healthy = False
    return jsonify({"status": f"health set to {status}"}), 200

@app.route('/set_ready/<status>', methods=['POST'])
def set_ready(status):
    global is_ready
    if status == 'ready':
        is_ready = True
    elif status == 'notready':
        is_ready = False
    return jsonify({"status": f"readiness set to {status}"}), 200



# Define un endpoint /notes que acepta solicitudes POST
@app.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    new_note = Note(title=data['title'], description=data['description'])
    db.session.add(new_note)
    db.session.commit()
    logger.info(f'Note added: {new_note.title}')
    return jsonify({"message": f"Note '{new_note.title}' added."}), 201

#Define un endpoint /notes que acepta solicitudes GET
@app.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    notes_list = [{"title": note.title, "description": note.description} for note in notes]
    logger.info(f'Retrieved {len(notes_list)} notes.')
    return jsonify(notes_list)

# Intentar conectar a la base de datos con reintentos
def wait_for_db():
    max_retries = 10
    for i in range(max_retries):
        try:
            db.create_all()  # Crear las tablas si no existen
            print("Database is ready.")
            return
        except OperationalError:
            print("Database not ready yet. Retrying...")
            time.sleep(5)
    raise RuntimeError("Database is not available after several retries.")

if __name__ == '__main__':
    wait_for_db()
    app.run(host='0.0.0.0', port=5000)

