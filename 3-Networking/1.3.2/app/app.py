from flask import Flask
import redis

app = Flask(__name__)

# Configura la conexión a Redis
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    # Incrementa el contador en Redis
    count = redis_client.incr('counter')
    return f'Hello! You are visitor number {count}.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
