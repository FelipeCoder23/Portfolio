FROM python:3.10-slim

WORKDIR /app

# Instalar git en la imagen Docker. Necesitarás también instalar los paquetes necesarios para que pip pueda compilar cualquier dependencia que lo requiera.
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt

# Instalar las dependencias de Python usando pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "80"]
