agenda = {
    "Ana": "3001112233",
    "Bruno": "3154445566",
    "Carla": "3017778899"
}

del agenda["Ana"]
agenda["Juan"] = "3002020202"

nombre = input("Ingrese el nombre de la persona")
#Mostrar el número de un contacto espcífico

if nombre in agenda:
    print("Teléfono de " + nombre, agenda[nombre])

else:
    telefono = input("Ingrese el teléfono")
    agenda[nombre] = telefono

print("Diccionario completo", agenda)

estudiantes = {
    "Lucía": [4.5, 3.8, 4.2],
    "Mateo": [3.0, 3.5, 4.0, 4.2],
    "Sofía": [5.0, 4.8, 4.9],
}

promedios = {}
for nombre, notas in estudiantes.items():
    print(nombre, notas)
    prom = sum(notas) / len (notas)
    print(f"Promedio de {nombre}: {prom:.2f}")
    promedios[nombre] = prom
print(promedios)

mejor_estudiante = max(promedios, key=promedios.get)
print(mejor_estudiante, promedios[mejor_estudiante])
