FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "80"]
