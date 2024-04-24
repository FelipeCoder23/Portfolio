FROM python:3.10-slim

WORKDIR /app

# Instala las librerías necesarias del sistema
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "80"]
