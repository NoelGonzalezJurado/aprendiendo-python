videojuego1 = {
    "titulo" : "Europa Universalis 4",
    "puntuacion" : 8
}

videojuego2 = {
    "titulo" : "Stellaris",
    "puntuacion" : 9
}

videojuego3 = {
    "titulo" : "Inazuma eleven VR",
    "puntuacion" : 6
}

videojuego4 = {
    "titulo" : "Life is Feudal",
    "puntuacion" : 4
}

videojuegos = [videojuego1, videojuego2, videojuego3, videojuego4]

for videojuego in videojuegos:
    if videojuego["puntuacion"] >= 7 :

        print(f"{videojuego['titulo']}: {videojuego['puntuacion']}")
