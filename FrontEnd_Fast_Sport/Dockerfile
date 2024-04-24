FROM python:3.9-slim

WORKDIR /app

# Copiar solo lo necesario para instalar las dependencias
COPY ./requirements.txt /app/requirements.txt

# Instalar las dependencias de Python usando pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar el resto de los archivos necesarios
COPY . /app

# Comando para ejecutar la aplicación Streamlit
CMD ["streamlit", "run", "front.py", "--server.port=8501", "--server.address=0.0.0.0"]
