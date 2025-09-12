class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuenta = cuenta
        self.cuentas.append(cuenta)

class Cuenta:
    def __init__(self, numero, oficina):
        self.numero = numero
        self.oficina = oficina
        self.saldo = 0
    
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad

#Crear una instancia (objeto) de la clase Persona
persona1 = Persona("Juan", 35)
print("El nombre de la persona es ", persona1.nombre)
print(f"La edad de la persona es {persona1.edad}")

#Crear una instancia (objeto) de la clase Cuenta
cuenta1 = Cuenta("123456789", "Oficina 1")
print("El número de la cuenta es:", cuenta1.numero)
print(f"La oficina de la cuenta es {cuenta1.oficina}")

#Asociar la cuenta a la persona
persona1.agregar_cuenta(cuenta1)

cuenta2 = Cuenta("234234234", "Oficina 2")

persona1.agregar_cuenta(cuenta2)

persona1.cuentas[0].depositar(1000)

print(persona1.cuentas[0].saldo)

persona1.cuentas[0].depositar(500)
print(persona1.cuentas[0].saldo)
print(persona1.cuentas[1].saldo)