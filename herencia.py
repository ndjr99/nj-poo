class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hacer_sonido(self):
        pass

    def orinar(self):
        print(f"{self.nombre} está orinando.")
    
class Perro(Animal):
    def __init__(self, nombre, color_pelota):
        super().__init__(nombre)
        self.color_pelota = color_pelota
        
    def hacer_sonido(self):
        print(f"{self.nombre} hace guau guau")

    def salir_a_pasear(self):
        print(f"{self.nombre} está paseando")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace miau miau")

animal1 = Perro("Mia", "Rojo")
animal1.hacer_sonido()
animal1.salir_a_pasear()
animal1.orinar()

animal2 = Gato("Simba")
animal2.hacer_sonido()
animal2.orinar()

print(isinstance(animal1, Perro))
print(isinstance(animal1, Animal))
print(issubclass(Perro, Gato))
print(issubclass(Gato, Animal))