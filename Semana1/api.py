
import requests

ciudad = input("¿De qué ciudad quieres saber el tiempo? ")
respuesta = requests.get(f"https://wttr.in/{ciudad}?format=j1")

if respuesta.status_code == 200:
    datos = respuesta.json()
    temp = datos["current_condition"][0]["temp_C"]
    desc = datos["current_condition"][0]["weatherDesc"][0]["value"]
    humedad = datos["current_condition"][0]["humidity"]
    sensacion = datos["current_condition"][0]["FeelsLikeC"]

    print(f"El tiempo en {ciudad}:")
    print(f"Temperatura: {temp}°C")
    print(f"Sensación térmica: {sensacion}°C")
    print(f"Humedad: {humedad}%")
    print(f"Estado: {desc}")
else:
    print(f"No se encontró la ciudad: {ciudad}")