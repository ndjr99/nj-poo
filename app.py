class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("El perro que esta ladrando es: ", self.nombre)
    
class Persona:
    def _init_(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        
#Vamos a instanciar un objeto desde la clase Perro
print("Mi primer perrito:")
mi_perrito = Perro("Mia", "Golden")
print(mi_perrito.nombre)
print(mi_perrito.raza)

print("Mi segundo perrito:")
otro_perrito = Perro("Happy", "Criolla")
print(otro_perrito.nombre)
print(otro_perrito.raza)

nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")
tercer_perrito = Perro(nombre, raza)
print("Tercer perrito:")
print(tercer_perrito.nombre)
print(tercer_perrito.raza)

print("Ahora los perros van a ladrar")
mi_perrito.ladrar()
otro_perrito.ladrar()
tercer_perrito.ladrar()