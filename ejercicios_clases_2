class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def mostrar_productos(self):
        print("Nombre del producto:", self.nombre)
        print("Precio del producto:", self.precio)
        print("Cantidad disponible:", self.cantidad_disponible)
        print()

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad_disponible:
            self.cantidad_disponible -= cantidad_vendida
            print("Venta realizada con éxito")
            print("Total de la venta:", self.precio * cantidad_vendida)
            print(f"Cantidad restante de {self.nombre}: {self.cantidad_disponible}")
        else:
            print("No hay suficiente cantidad de", self.nombre)    

print("Gestión de productos")
lista_productos = []
while True:
    print("Seleccione la opción deseada")
    print("1. Agregar producto")
    print("2. Mostrar información de productos")
    print("3. Realizar venta")
    print("0. Salir")
    print()
    opcion = int(input())

    if opcion == 1:
        print("Ingrese el nombre del producto")
        nombre = input()
        print("Ingrese el precio del producto")
        precio = float(input())
        print("Ingrese la cantidad disponible del producto")
        cantidad_disponible = int(input())
        producto = Producto(nombre, precio, cantidad_disponible)
        lista_productos.append(producto)
        print("Producto registrado correctamente")
        print()

    elif opcion == 2:
        numero_productos = len(lista_productos)
        print("El número de productos es:", numero_productos)
        print()
        for producto in lista_productos:
            producto.mostrar_productos()

    elif opcion == 3:
        print("Ingrese el nombre del producto a vender")
        producto_vendido = input()
        for producto in lista_productos:
            if producto.nombre.lower() == producto_vendido.lower():
                print("Ingrese la cantidad a vender")
                cantidad_vendida = int(input())
                if cantidad_vendida <= 0:
                    print("La cantidad a vender debe ser mayor que cero.")
                    print()
                    break
                producto.vender(cantidad_vendida)
                print()
                break
        else:
            print("Producto no encontrado")
            print()
                
    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opción no válida")
        print()
        