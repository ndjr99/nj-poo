class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def respirar(self):
        print(f"{self.nombre} está respirando")

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}")    

persona1 = Persona("Juan")
persona1.respirar()

persona2 = Estudiante("Camila", "Ingeniería de sistemas")
persona2.estudiar()