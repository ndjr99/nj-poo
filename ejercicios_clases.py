class Estudiante:
    def __init__(self,nombre, edad, nota1, nota2, nota3):
        self.nombre = nombre
        self.edad = edad
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.nombre)
        print("Nota1: ", self.nota1)
        print("Nota2: ", self.nota2)
        print("Nota3: ", self.nota3)

    def calcular_promedio(self):
        promedio = (self.nota1 + self.nota2 + self.nota3) / 3
        return promedio
    
print("Bienvenido a la gestión de estudiantes")
print("Ingrese el nombre del estudiante")
nombre = input()
print("Ingrese la edad del estudiante")
edad = int(input())
print("Ingrese la primera nota")
nota1 = float(input())
print("Ingrese la segunda nota")
nota2 = float(input())
print("Ingrese la tercera nota")
nota3 = float(input())
estudiante = Estudiante(nombre, edad, nota1, nota2, nota3)

promedio_estudiante = estudiante.calcular_promedio()
print("El promedio de ", estudiante.nombre, "es ", promedio_estudiante)