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

db = SQLAlchemy(app)

# Modelo de la base de datos
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Note {self.title}>'

@app.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    new_note = Note(title=data['title'], description=data['description'])
    db.session.add(new_note)
    db.session.commit()
    logger.info(f'Note added: {new_note.title}')
    return jsonify({"message": f"Note '{new_note.title}' added."}), 201

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

