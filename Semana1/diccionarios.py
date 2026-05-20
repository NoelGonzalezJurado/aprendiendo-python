persona = {
    "nombre": "Noel",
    "edad": 23,
    "ciudad": "Barcelona"
}

print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])

persona["profesion"] = "programador"
persona["edad"] = 24

print(persona)

for clave, valor in persona.items():
    print(f"{clave}: {valor}")



videojuego = {
    "titulo" : "Europa Universalis 4",
    "genero" : "Conquista, exploració, dominio",
    "año" : 2016,
    "puntuacion": 8 
}

for clave,valor in videojuego.items():
    print(f"{clave} : {valor}")