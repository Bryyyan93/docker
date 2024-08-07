from flask import Flask
import redis
import os

app = Flask(__name__)

# Configura la conexión a Redis
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    # Incrementa el contador en Redis
    count = redis_client.incr('counter')
    message = f'Hello! You are visitor number {count}.'
    
    # Escribir el log en un archivo si está en modo desarrollo
    if os.getenv('FLASK_ENV') == 'development':
        with open('/logs/log.txt', 'a') as log_file:
            log_file.write(f'{message}\n')
    
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
