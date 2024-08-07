# Usa la imagen base de Python 3.7 Alpine
FROM python:3.7-alpine

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de la aplicación al contenedor
COPY app.py .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 para Flask
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
