# Fase 1: Compilación e instalación de dependencias
FROM python:3.8-slim as build

WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Fase 2: Construcción de la imagen final
FROM python:3.8-slim

WORKDIR /app

# Copiar las dependencias desde la fase anterior
COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copiar el código fuente
COPY app.py .
COPY config.py .

# Exponer el puerto de la aplicación
EXPOSE 5000

# Comando por defecto
CMD ["python", "app.py"]
