# Aprendiendo Python 🐍

Mi viaje aprendiendo Python desde cero hasta DAM en septiembre 2026.

## Estructura

- **Semana1/** → Fundamentos: variables, bucles, funciones, diccionarios, APIs
- **Semana2/** → FastAPI: API REST completa con base de datos SQLite

## Semana 2 - API de Tareas

API REST completa construida con FastAPI y SQLAlchemy.

### Instalación

```bash
pip install fastapi uvicorn sqlalchemy
cd Semana2
uvicorn main:app --reload
```

### Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /tareas | Listar todas las tareas |
| GET | /tareas/{id} | Buscar tarea por id |
| POST | /tareas | Crear tarea |
| PUT | /tareas/{id} | Editar tarea |
| DELETE | /tareas/{id} | Borrar tarea |

### Documentación interactiva

Con el servidor corriendo, visita: http://127.0.0.1:8000/docs