class Libreria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.ultima_venta = None

    def agregar_libro(self, nombre_libro):
        self.libros.append(nombre_libro)
        print("Libro agregado exitosamente")

    def registrar_venta(self, cliente, total):
        self.ultima_venta = (cliente, total)

    def mostrar_libros(self):
        for i in range (0, len(self.libros)):
            print("El libro número", i + 1, "es", self.libros[i])

print("Bienvenido al programa de librerías")
librerias = []
while True:
    print("Seleccione la opción deseada")
    print("1. Crear librería")
    print("2. Agregar un libro a una librería")
    print("3. Mostrar libros de una librería")
    print("4. Todas las librerías con sus libros")
    opcion = int(input())
    if opcion == 1:
        nombre = input("Ingresa el nombre de la librería ").lower()
        nueva_libreria = Libreria(nombre)
        librerias.append(nueva_libreria)
    elif opcion == 2:
        nombre = input("Ingresa el nombre de la librería ").lower()
        existe = False
        for libreria in librerias:
            if libreria.nombre == nombre:
                existe = True
                nombre_libro = input("Ingresa el nombre del libro ").lower()
                libreria.agregar_libro(nombre_libro)
        if existe == False:
            print("No existe esta librería")
    elif opcion == 3:
        nombre = input("Ingresa el nombre de la librería ").lower()
        existe = False
        for libreria in librerias:
            if libreria.nombre == nombre:
                existe = True
                libreria.mostrar_libros()
        if existe == False:
            print("No existe esta librería")
    elif opcion == 4:
        for libreria in librerias:
            print(libreria.nombre)
            libreria.mostrar_libros()
    elif opcion == 0:
        break
    else:
        print("Opción incorrecta")