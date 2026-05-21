from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Tarea(BaseModel):
    titulo: str
    completada: bool = False

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

tareas = []

@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    nueva = {"id": len(tareas) + 1, **tarea.model_dump()}
    tareas.append(nueva)
    return nueva

@app.get("/tareas")
def listar_tareas():
    return tareas

@app.delete("/tareas/{id}")
def borrar_tarea(id: int):
    for i, tarea in enumerate(tareas):
        if tarea["id"] == id:
            tareas.pop(i)
            return {"mensaje": f"Tarea {id} eliminada"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.put("/tareas/{id}")
def editar_tarea(id: int, tarea_actualizada: Tarea):
    for i, tarea in enumerate(tareas):
        if tarea["id"] == id:
            tareas[i] = {"id": id, **tarea_actualizada.model_dump()}
            return tareas[i]
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.get("/tareas/{id}")
def buscar_tarea(id: int):
    for i, tarea in enumerate (tareas):
        if tarea ["id"] == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")