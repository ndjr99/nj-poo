class Motor:
    def __init__(self):
        self.encendido = False

    def encender(self):
        self.encendido = True
        print("El motor ha sido encendido.\n")

    def apagar(self):
        self.encendido = False
        print("El motor ha sido apagado.\n")

class Vehiculo:
    def __init__(self, placa):
        self.placa = placa
        self.motor = Motor()
        self.servicio = False

    def poner_en_servicio(self):
        self.servicio = True
        print("El vehiculo ha sido puesto en servicio.\n")

    def sacar_de_servicio(self):
        self.servicio = False
        print("El vehiculo ha sido sacado de servicio.\n")

class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.placa} agregado a la flota.\n")

    def quitar_vehiculo(self, vehiculo):
        self.vehiculos.remove(vehiculo)
        print(f"Vehículo {vehiculo.placa} quitado de la flota.\n")
    
    def consultar_vehiculo(self, placa):
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa:
                return vehiculo
        else:
            return None

    def reporte(self):

        for vehiculo in self.vehiculos:
            print(f"Vehículo: {vehiculo.placa}:")
            if vehiculo.servicio == True:
                print("Está en servicio.")
            else:
                print("No está en servicio.")
            if vehiculo.motor.encendido == True:
                print("El motor está encendido.\n")
            else:
                print("El motor está apagado.\n")

flota = Flota()

while True:
    print("Bienvenido al sistema de gestión de la flota.\n")
    print("Seleccione una opción:")
    print("1. Agregar vehículo.")
    print("2. Quitar vehículo.")
    print("3. Poner vehículo en servicio.")
    print("4. Sacar vehículo de servicio.")
    print("5. Encender motor de vehículo.")
    print("6. Apagar motor de vehículo.")
    print("7. Consultar vehículo.")
    print("8. Reporte de flota.")
    print("0. Salir.\n")
    opcion = input("Ingrese la opción deseada: ")
    print()

    if opcion == "1":
        placa = input("Ingrese la placa del vehículo: ").upper()
        existe = False
        for vehiculo in flota.vehiculos:
            if vehiculo.placa == placa:
                existe = True
                print("El vehículo ya está en la flota.\n")
                break
        if existe == False:
            vehiculo = Vehiculo(placa)
            flota.agregar_vehiculo(vehiculo)

    elif opcion == "2":
        placa = input("Ingrese la placa del vehículo a quitar: ").upper()
        for vehiculo in flota.vehiculos:
            if vehiculo.placa == placa:
                flota.quitar_vehiculo(vehiculo)
                break
        else:
            print("Vehículo no encontrado")

    elif opcion == "3":
        placa = input("Ingrese la placa del vehículo a poner en servicio: ").upper()
        for vehiculo in flota.vehiculos:
            if vehiculo.placa == placa:
                if vehiculo.servicio == False:
                    vehiculo.poner_en_servicio()
                else:
                    print("El vehículo ya había sido puesto en servicio.\n")
                break
        else:
            print("Vehículo no encontrado.\n")

    elif opcion == "4":
        placa = input("Ingrese la placa del vehículo a sacar de servicio: ").upper()
        for vehiculo in flota.vehiculos:
            if vehiculo.placa == placa:
                if vehiculo.servicio == True:
                    vehiculo.sacar_de_servicio()
                else:
                    print("El vehículo ya había sido sacado de servicio.\n")
                break
        else:
            print("Vehículo no encontrado.\n")

    elif opcion == "5":
        placa = input("Ingrese la placa del vehículo al que desea encender el motor: ").upper()
        for vehiculo in flota.vehiculos:
            if vehiculo.placa == placa:
                if vehiculo.motor.encendido == False:
                    vehiculo.motor.encender()
                else:
                    print("El vehículo ya tenía el motor encendido.\n")
                break
        else:
            print("Vehículo no encontrado.\n")

    elif opcion == "6":
        placa = input("Ingrese la placa del vehículo al que desea apagar el motor: ").upper()
        for vehiculo in flota.vehiculos:
            if vehiculo.placa == placa:
                if vehiculo.motor.encendido == True:
                    vehiculo.motor.apagar()
                else:
                    print("El vehículo ya tenía el motor apagado.\n")
                break
        else:
            print("Vehículo no encontrado.\n")

    elif opcion == "7":
        placa = input("Ingrese la placa del vehículo que desea consultar: ").upper()
        vehiculo = flota.consultar_vehiculo(placa)
        if vehiculo != None:
            print(f"Vehículo: {vehiculo.placa}")
            if vehiculo.servicio == True:
                print("Está en servicio.")
            else:
                print("No está en servicio.")
            if vehiculo.motor.encendido == True:
                print("El motor está encendido.\n")
            else:
                print("El motor está apagado.\n")
        else:
            print(f"El vehiculo {placa} no se encuentra en la flota.\n")

    elif opcion == "8":
        if flota.vehiculos:
            total_vehiculos = len(flota.vehiculos)
            print(f"Total de vehículos: {total_vehiculos}\n")
            flota.reporte()
        else:
            print("La flota está vacía.\n")
    
    elif opcion == "0":
        print("Hasta luego.\n")
        break
    
    else:
        print("Opción inválida.\n")