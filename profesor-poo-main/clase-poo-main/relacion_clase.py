class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota 

class Profesor:
    def __init__(self, nombre, edad, experiencia):
        self.nombre = nombre
        self.edad = edad
        self.experiencia = experiencia 

class GrupoAsignatura:
    def __init__(self, nombre, horario, codigo, profesor):
        self.nombre = nombre
        self.horario = horario
        self.codigo = codigo
        self.profesor = profesor
        self.estudiantes = []

    def Agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print("Estudiante agregado exitosamente")

    def promedio(self):
        acumulador = 0
        for estudiante in self.estudiantes:
            acumulador = acumulador + estudiante.nota
        promedio = acumulador/len(self.estudiantes)
        return promedio
    
    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)
    

profesor = Profesor("Juan Esteban", 35, 5)
poo = GrupoAsignatura("Programación Orientada a Objetos", "M-V 10-12", 62, profesor)
estudiante1 = Estudiante("Esteban Díaz", 17, 5)
estudiante2 = Estudiante("Jorge", 20, 2.5)
estudiante3 = Estudiante("Luis", 21, 3)

poo.Agregar_estudiante(estudiante1)

poo.Agregar_estudiante(estudiante2)

poo.Agregar_estudiante(estudiante3)

print(poo.promedio())
poo.mostrar_estudiantes()