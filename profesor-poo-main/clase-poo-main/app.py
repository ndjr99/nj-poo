class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza 

    def ladrar(self):
        print("El perro que esta ladrando es: ", self.nombre)

class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo 


#Vamos a instanciar un objeto desde la clase Perro
print("Mi primer perrito:")
mi_perrito = Perro("Mia", "Golden")
print(mi_perrito.nombre)
print(mi_perrito.raza)

print("Mi segundo perrito:")
mi_otro_perrito = Perro("Paul", "Pug")
print(mi_otro_perrito.nombre)
print(mi_otro_perrito.raza)

print("Ingrese los datos del tercer perrito:")
nombre = input("Ingrese el nombre")
raza = input("Ingrese la raza")

mi_tercer_perrito = Perro(nombre, raza)
print("Los datos del tercer perrito son:")
print(mi_tercer_perrito.nombre)
print(mi_tercer_perrito.raza)

print("Ahora los perros van a ladrar")
mi_perrito.ladrar()
mi_otro_perrito.ladrar()
mi_tercer_perrito.ladrar()

