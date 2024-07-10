# Dockerfile

# Usa la imagen base de Python 3.9
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copia el archivo requirements.txt al directorio de trabajo del contenedor
COPY requirements.txt .

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copia todo el contenido actual del directorio local al directorio de trabajo del contenedor
COPY . .

# Comando por defecto para ejecutar tu aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]