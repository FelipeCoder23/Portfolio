from fastapi import FastAPI, File, UploadFile
import subprocess
import shutil
from predict import run_yolov5_detection


app = FastAPI()

@app.get('/')
def root():
    return {'estado': 'Funciona'}

@app.post("/predict_video")  # Cambiado a POST pararun_yolov5_detection manejar la carga de archivos
async def predict(file: UploadFile = File(...)):
    local_filename = "video_bonit.mp4"
    with open(local_filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Asegúrate de que la ruta al modelo y al archivo de entrada sean correctas
    response = run_yolov5_detection(local_filename)

    tiempos = []
    # Asegúrate de que la ruta al archivo tiempos_goles.txt sea la correcta
    with open('detection_times.txt') as f:
        tiempos = [line.strip() for line in f.readlines()]

    return {'prediction': tiempos}
    