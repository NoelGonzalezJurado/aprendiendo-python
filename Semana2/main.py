from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola desde mi primera API"}

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

@app.get("/buscar")
def buscar(ciudad: str, limite: int = 3):
    return {
        "ciudad": ciudad,
        "limite": limite,
        "mensaje": f"Buscando {limite} resultados para {ciudad}"
    }