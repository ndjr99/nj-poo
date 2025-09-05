class Motor:
    def __init__(self, motor):
        self.motor = motor

    def enceder(self):
        print("El motor ha sido encendido")

    def apagar(self):
        print("El motor ha sido apagado")

class Vehiculos:
    def __init__(self, placa_vehiculo, motor):
        self.placa = placa_vehiculo
        self.motor = motor

class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, placa_vehiculo):
        self.vehiculos.append(placa_vehiculo)

    def quitar_vehiculo(self, placa_vehiculo):
        self.vehiculos.remove(placa_vehiculo)
    
    def buscar_vehiculo(self, placa_vehiculo):
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa_vehiculo:
                return vehiculo
        else:
            print("El vehiculo no se encuentra en la flota")

    def reporte(self):
        for vehiculo in self.vehiculos:
            print(vehiculo.placa)