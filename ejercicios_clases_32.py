import random

class Cuenta:
    def __init__(self, titular):
        self.titular = titular
        self.cuenta = random.randint(100, 999)
        self.saldo = 0

    def mostrar_cuentas(self):
        print("Número de cuenta:", self.cuenta)
        print("Titular de la cuenta:", self.titular)
        print("Saldo actual:", self.saldo)
        print()

    def depositar(self, deposito):
        if deposito > 0:
            self.saldo += deposito
            print(f"Depósito realizado. Nuevo saldo: {self.saldo}")
        else:
            print("El depósito debe ser mayor a 0.")

    def retirar(self, retiro):
        if 0 < retiro <= self.saldo:
            self.saldo -= retiro
            print(f"Retiro realizado. Nuevo saldo: {self.saldo}")
        else:
            print("El retiro debe ser mayor a 0 y no puede exceder el saldo actual.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

print("Bienvenido a la gestión de cuentas bancarias")
lista_cuentas = []
while True:
    print("Seleccione la opción deseada")
    print("1. Agregar cuenta")
    print("2. Mostrar información de cuentas")
    print("3. Depositar dinero")
    print("4. Retirar dinero")
    print("5. Consultar saldo")
    print("0. Salir")
    opcion = int(input())
    
    if opcion == 1:
        print("Ingrese el nombre del titular de la cuenta")    
        titular = input()                
        nueva_cuenta = Cuenta(titular)
        lista_cuentas.append(nueva_cuenta)
        print("Cuenta registrada correctamente, su numero de cuenta es: ", nueva_cuenta.cuenta)
        print()

    elif opcion == 2:
        numero_cuentas = len(lista_cuentas)
        print("El número de cuentas es:", numero_cuentas)
        print()
        for cuenta in lista_cuentas:
            cuenta.mostrar_cuentas()
            
    elif opcion == 3:
        cuenta = int(input("Ingrese el número de cuenta: "))
        for cuentas in lista_cuentas:
            if cuentas.cuenta == cuenta:
                deposito = float(input("Ingrese la cantidad a depositar: "))  
                cuentas.depositar(deposito)
                print()
                break  
        else:
            print("La cuenta no existe.")
            print()  
            
    elif opcion == 4:
        cuenta = int(input("Ingrese el número de cuenta: "))
        for cuentas in lista_cuentas:
            if cuentas.cuenta == cuenta:
                retiro = float(input("Ingrese la cantidad a retirar: "))  
                cuentas.retirar(retiro)
                print()
                break  
        else:
            print("La cuenta no existe.")
            print()
    elif opcion == 5:
        cuenta = int(input("Ingrese el número de cuenta: "))
        for cuentas in lista_cuentas:
            if cuentas.cuenta == cuenta: 
                cuentas.consultar_saldo()
                print()
                break
        else:
            print("La cuenta no existe.")               
            print()
            
    elif opcion == 0:
        print("Hasta luego.")
        break
        
    else:
        print("Opción no válida.")
        print()