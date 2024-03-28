# prediction.py
# Este es un script de predicción simulado que simplemente escribe tiempos de eventos ficticios en un archivo.

# Simulando tiempos de eventos (por ejemplo, goles) en formato "Gol HH:MM:SS"
eventos_simulados = [
    "Gol 00:02:10",
    "Gol 00:05:00"
]

# Escribir los eventos simulados en un archivo de texto
with open('tiempos_goles.txt', 'w') as f:
    for evento in eventos_simulados:
        f.write(f"{evento}\n")

print("Predicciones simuladas generadas con éxito.")
