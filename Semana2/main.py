from fastapi import FastAPI

app = FastAPI()

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola {nombre}, bienvenido a mi API"}

@app.get("/clima/{ciudad}")
def clima(ciudad: str):
    import requests
    respuesta = requests.get(f"https://wttr.in/{ciudad}?format=j1")
    datos = respuesta.json()
    temp = datos["current_condition"][0]["temp_C"]
    desc = datos["current_condition"][0]["weatherDesc"][0]["value"]
    return {"ciudad": ciudad, "temperatura": temp, "estado": desc}