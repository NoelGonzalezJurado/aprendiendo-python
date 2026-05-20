def saludar(nombre):
    print(f"Hola {nombre}, bienvenido!")

saludar("Noel")
saludar("Maria")
saludar("Carlos")

def sumar(a, b):
    resultado = a + b
    return resultado

print(sumar(3, 5))
print(sumar(10, 20))

total = sumar(10, 20)
print(f"El total es {total}")


def area_rectangulo(ancho, alto):
    resultado = (ancho * alto)
    return resultado

print(area_rectangulo (5, 7))
print(area_rectangulo (4, 8))




def suma_total(numeros):
    resultado = 0
    for numero in numeros:     
        resultado = resultado + numero
        
    return resultado    
numeros = [5, 10, 15, 20]

print(suma_total(numeros))

