class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False

    def encender(self):
        self.estado = True
        print(self.nombre, "encendido")

    def apagar(self):
        self.estado = False
        print(self.nombre, "apagado")

class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__dispositivos = []

    def agregard(self, dispositivo):
        self.__dispositivos.append(dispositivo)
        print("Dispositivo agregado")

    def mostrard(self):
        for dispositivo in self.__dispositivos:
            print(dispositivo.nombre)

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.__espacios = []

    def agregare(self, nombre):
        self.__espacios.append(Espacio(nombre))
        print("Espacio agregado")

    def buscare(self, nombre):
        for espacio in self.__espacios:
            if espacio.nombre == nombre:
                return espacio
        return None

    def mostrare(self):
        for espacio in self.__espacios:
            print(espacio.nombre)



mi_casa = Casa("Calle 123")
mi_casa.agregare("Cocina")
mi_casa.agregare("Habitación")
mi_casa.agregare("Baño")
television = Dispositivo("Television")
mi_casa.buscare("Habitación").agregard(television)
mi_casa.buscare("Habitación").mostrard()