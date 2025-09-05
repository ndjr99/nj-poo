inventario = {}

print("Bienvenido al programa")
while True:
    print("1. Agregar productos")
    print("2. Vender productos")
    print("3. Mostrar inventario")
    print("0. Salir")

    opcion = int(input())

    if opcion == 1:
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))

        if nombre_producto in inventario:
            inventario[nombre_producto] += cantidad
        else:
            inventario[nombre_producto] = cantidad

        print("Inventario actualizado!")

    elif opcion == 2:
        producto = input("Ingrese el nombre del producto a vender: ")

        if nombre_producto in inventario:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if inventario[nombre_producto] >= cantidad:
                inventario[nombre_producto] -= cantidad
                print("Inventario actualizado!")
            else:
                print("No hay cantidad del producto")
        else:
            print("El producto no existe")
    elif opcion == 3:
        print(inventario)
    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opción no válida")