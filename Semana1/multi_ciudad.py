import requests

ciudades = []

for i in range(3):
    ciudad = input(f"Ciudad {i+1}: ")
    ciudades.append(ciudad)

for ciudad in ciudades:
    respuesta = requests.get(f"https://wttr.in/{ciudad}?format=j1")
    datos = respuesta.json()
    temp = datos["current_condition"][0]["temp_C"]
    print(f"{ciudad}: {temp}°C")
