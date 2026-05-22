from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TareaSchema(BaseModel):
    titulo: str = Field(min_length=3, max_length=100, description="Título de la tarea")
    completada: bool = Field(default=False, description="Si la tarea está completada")
    categoria_id: int | None = Field(default=None, description="ID de la categoría")

class CategoriaSchema(BaseModel):
    nombre: str = Field(min_length=3, max_length=50, description="Nombre de la categoría")

class CategoriaResponse(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True

class TareaResponse(BaseModel):
    id: int
    titulo: str
    completada: bool
    categoria: CategoriaResponse | None = None

    class Config:
        from_attributes = True


@app.get("/tareas", response_model=list[TareaResponse])
def listar_tareas(db: Session = Depends(get_db)):
    return db.query(models.Tarea).all()

@app.post("/tareas")
def crear_tarea(tarea: TareaSchema, db: Session = Depends(get_db)):
    nueva = models.Tarea(**tarea.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@app.get("/tareas/{id}")
def buscar_tarea(id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.Tarea).filter(models.Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@app.delete("/tareas/{id}")
def borrar_tarea(id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.Tarea).filter(models.Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(tarea)
    db.commit()
    return {"mensaje": f"Tarea {id} eliminada"}

@app.put("/tareas/{id}")
def editar_tarea(id: int, tarea_actualizada: TareaSchema, db: Session = Depends(get_db)):
    tarea = db.query(models.Tarea).filter(models.Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea.titulo = tarea_actualizada.titulo
    tarea.completada = tarea_actualizada.completada
    db.commit()
    db.refresh(tarea)
    return tarea

@app.post("/categorias")
def crear_categoria(categoria: CategoriaSchema, db: Session = Depends(get_db)):
    nueva = models.Categoria(**categoria.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@app.get("/categorias")
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(models.Categoria).all()

@app.get("/categorias/{id}/tareas")
def  listar_tareas_por_categoria( id: int, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria.tareas

