class Estudiante:
    def __init__(self, nombre, edad, nota1, nota2, nota3):
        self.nombre = nombre
        self.edad = edad
        self.nota1 = nota1 
        self.nota2 = nota2 
        self.nota3 = nota3 

    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota1: ", self.nota1)
        print("Nota2: ", self.nota2)
        print("Nota3: ", self.nota3)

    def calcular_promedio(self):
        promedio = (self.nota1 + self.nota2 + self.nota3) / 3
        return promedio
    
print("Bienvenido al sistema de gestión de estudiantes")
lista_estudiantes = []
while True:
    print("Seleccione la opción deseada")
    print("1. Agregar estudiante")
    print("2. Mostrar información de estudiantes")
    print("0. Salir")
    opcion = int(input())
    if opcion == 1:
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
        lista_estudiantes.append(estudiante)
        print("Estudiante registrado correctamente")
    elif opcion == 2:
        numero_estudiantes = len(lista_estudiantes)
        print("El número de estudiantes es: ", numero_estudiantes)
        for estudiante in lista_estudiantes:
            print("El nombre del estudiante es ", estudiante.nombre)
            print("El promedio del estudiante es", estudiante.calcular_promedio())
    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opción no válida")