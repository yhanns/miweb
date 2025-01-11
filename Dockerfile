# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará Flask (5000 por defecto)
EXPOSE 5000

# Define el comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
