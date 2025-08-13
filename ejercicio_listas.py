import random

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numeros = [random.randint(100, 999) for _ in range(5)]

persona1 = Persona("Juan Esteban")
persona2 = Persona("Isaac")

print("Los números para ", persona1.nombre, "son ", persona1.numeros)
print("Los números para ", persona2.nombre, "son ", persona2.numeros)