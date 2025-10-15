#Crear lista
mi_lista = ["primer elemento", "segundo elemento", "tercer elemento"]
print(mi_lista[1:])


#Crear lista con ceros
lista_ceros = [0] * 10
print(lista_ceros)

import random

lista_random = []

for i in range(0, 10):
    lista_random.append(random.randint(1, 100))
print(lista_random)


lista_random2 = [random.randint(1, 100) for _ in range(10)]
print(lista_random2)

lista_ejemplo = [i for i in range(0,10)]
print(lista_ejemplo)

lista_ejemplo[2] = 1
lista_ejemplo[5] = 2

print(lista_ejemplo)

#Eliminar un elemento
# lista_ejemplo.remove(1)
# print(lista_ejemplo)

# #Eliminar por posición
# del lista_ejemplo[2]
# print(lista_ejemplo)

lista_ejemplo = [elemento for elemento in lista_ejemplo if elemento != 1]
print(lista_ejemplo)

lista_ejemplo.reverse()
print(lista_ejemplo)

lista_ejemplo.sort()
print(lista_ejemplo)

lista_ejemplo.sort(reverse=True)
print(lista_ejemplo)


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numeros = [random.randint(100, 999) for _ in range(5)]

persona1 = Persona("Juan Esteban")
person2 = Persona("Isaac")

print("Los números para ", persona1.nombre, "son ", persona1.numeros)
print("Los números para ", person2.nombre, "son ", person2.numeros)
