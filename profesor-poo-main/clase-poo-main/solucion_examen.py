class Libro:
    def __init__(self, autor, titulo, fecha, genero):
        self.autor = autor
        self.titulo = titulo
        self.fecha = fecha
        self.genero = genero

def buscar_libro(titulo, lista):
    existe = False
    for libro in lista:
        if libro.titulo == titulo:
            existe = True
    return existe


lista_libros = []
while True:
    print("Seleccione la opciòn deseada")
    print("1. Registrar libros")
    print("2. Mostrar libros")

    opcion = int(input())
    if opcion == 1:
        autor = input("Ingresar autor")
        titulo = input("Ingresar título")
        fecha = input("Ingresar fecha")
        genero = input("Ingresar genero")
        libro_nuevo = Libro(autor, titulo, fecha, genero)
        lista_libros.append(libro_nuevo)
        print("Libro agregado exitosamente")
    if opcion == 2:
        for libro in lista_libros:
            print(libro.autor)
            print(libro.titulo)
    if opcion == 3:
        titulo = input("Ingrese el nombre del libro")
        encontrado = buscar_libro(titulo, lista_libros)
        if encontrado == True:
            print("Lo encontré")
        else:
            print("No lo encontré")
    if opcion == 4:
        print("La cantidad de libros es", len(lista_libros))
    elif opcion == 0:
        break
