class Libro:
    def __init__(self, titulo, autor, año_publicacion, genero):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.genero = genero
    
lista_libros = []
print("Bienvenido a tu biblioteca personal")
while True:
    print("Seleccione una opción:")
    print("1. Registre un nuevo libro.")
    print("2. Listar todos los libros.")
    print("3. Consultar si un libro ya existe en la biblioteca.")
    print("4. Total de libros.")
    print("0. Salir")
    opcion = int(input())

    if opcion == 1:
        titulo = input("Ingrese el título del libro: ").lower()
        autor = input("Ingrese el autor del libro: ")
        año_publicacion = input("Ingrese el año de publicación del libro: ")
        genero = input("Ingrese el género del libro: ")
        libro = Libro(titulo, autor, año_publicacion, genero)
        lista_libros.append(libro)
        print("Libro registado correctamente.")

    elif opcion == 2:
        for libro in lista_libros:
            print(f"Titulo: {libro.titulo}")
            print(f"Autor: {libro.autor}")
            print(f"Año: {libro.año_publicacion}")
            print(f"Género: {libro.genero}")
            print()

    elif opcion == 3:
        titulo = input("Ingrese el título del libro: ").lower()
        existe = False
        for libro in lista_libros:
            if libro.titulo == titulo:
                existe = True
                print("El libro ya existe.")
        if existe == False:
            print("No existe este libro.")
    elif opcion == 4:
        numero_libros = len(lista_libros)
        print(numero_libros)
    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opción inválida")