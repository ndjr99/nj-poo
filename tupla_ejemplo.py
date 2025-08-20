tupla_ejemplo = (1, 10, 50, 4, 11, 12)
print(tupla_ejemplo[2])

#tupla_ejemplo[2] = 51

import random

tupla2 = tuple(random.randint(1, 100) for i in range (5))
print(tupla2)

numeros = [(100, 400, 321), (250, 324, 567)]

for numero in numeros:
    print(numero)