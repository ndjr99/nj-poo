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
personas = []
while True:
    print("1. Crear persona")
    print("2. Crear cuenta")
    print("3. Depositar")
    print("4. Mostrar cuentas por persona")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        nombre = input("Ingrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        persona = Persona(nombre, edad)
        personas.append(persona)
        print("Persona creada")

    elif opcion == 2:
        nombre = input("Ingrese el nombre de la persona: ")
        existe = False
        for persona in personas:
            if persona.nombre == nombre:
                existe = True
                numero = input("Ingrese el número de la cuenta: ")
                oficina = input("Ingrese la oficina: ")
                cuenta = Cuenta(numero, oficina)
                persona.agregar_cuenta(cuenta)
                print("Cuenta creada")
                break
        if not existe:
            print("Persona no encontrada")
            
    elif opcion == 3:
        nombre = input("Ingrese el nombre de la persona: ")
        existe = False
        for persona in personas:
            if persona.nombre == nombre:
                existe = True
                numero = input("Ingrese el número de la cuenta: ")
                for cuenta in persona.cuentas:
                    if cuenta.numero == numero:
                        print("La cuenta ya existe")
                        break

    elif opcion == 4:
        nombre = input("Ingrese el nombre de la persona: ")
        existe = False
        for persona in personas:
            if persona.nombre == nombre:
                existe = True
                numero = input("Ingrese el número de la cuenta: ")
                oficina = input("Ingrese la oficina de la cuenta: ")
                cuenta = Cuenta(numero, oficina)
                persona.agregar_cuenta(cuenta)
                print("Cuenta agregada a la persona")
                break
        if not existe:
            print("La persona no existe")