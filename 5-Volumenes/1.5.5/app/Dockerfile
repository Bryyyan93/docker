# Definir la imagen Docker para construir la aplicación
# Usa la imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY app.py .

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Establece valores por defecto para las variables de entorno
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

# Expone el puerto 5000 para Flask
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
