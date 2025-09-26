class Persona:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        return f"{self.nombre} ({self.nacionalidad})"

class Artista(Persona):
    def __init__(self, nombre, nacionalidad, genero_principal):
        super().__init__(nombre, nacionalidad)
        self.genero_principal = genero_principal
        self.canciones_independientes = []  # Canciones fuera de álbum
        self.albums = []  # Lista de álbumes

    def agregar_cancion(self, cancion):
        self.canciones_independientes.append(cancion)
        print(f"Se agregó la canción'{cancion.nombre}' a {self.nombre}")

    def agregar_album(self, album):
        self.albums.append(album)
        print(f"Se agregó el álbum '{album.nombre}' a {self.nombre}")

    def mostrar_discografia(self):
        print(f"Discografía de {self.nombre} ({self.genero_principal}):")
        if self.canciones_independientes:
            print("Canciones:")
            for i in self.canciones_independientes:
                print(f" - {i.nombre} ({i.duracion} min)")
        if self.albums:
            print("Álbumes:")
            for a in self.albums:
                print(f" - {a.nombre} ({a.año})")
                for i in a.canciones:
                    print(f"    * {i.nombre} ({i.duracion} min)")

class Cancion:
    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

class Album:
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
        self.canciones = []  # Composición: contiene canciones

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        print(f"Se agregó la canción '{cancion.nombre}' al álbum '{self.nombre}'")

class Discografia:
    def __init__(self):
        self.artistas = []  # Lista de artistas

    def agregar_artista(self, artista):
        self.artistas.append(artista)
        print(f"Se agregó el artista '{artista.nombre}' a la discografía")

    def buscar_artista(self, nombre):
        for a in self.artistas:
            if a.nombre.lower() == nombre.lower():
                return a
        return None

    def mostrar_todos_los_artistas(self):
        if not self.artistas:
            print("No hay artistas en la discografía")
            return
        print("Artistas en la discografía:")
        for a in self.artistas:
            print(f" - {a.nombre}")

def menu():
    discografia = Discografia()

    while True:
        print("Menú de Discografía")
        print("1. Agregar Artista")
        print("2. Agregar Canción Independiente a un Artista")
        print("3. Crear Álbum y agregar canciones")
        print("4. Mostrar Discografía de un Artista")
        print("5. Mostrar todos los Artistas")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del artista: ").strip()
            nacionalidad = input("Nacionalidad: ").strip()
            genero = input("Género principal: ").strip()
            artista = Artista(nombre, nacionalidad, genero)
            discografia.agregar_artista(artista)

        elif opcion == "2":
            nombre = input("Nombre del artista: ").strip()
            artista = discografia.buscar_artista(nombre)
            if artista:
                cancion_nombre = input("Nombre de la canción: ").strip()
                duracion = float(input("Duración en minutos: "))
                genero = input("Género: ").strip()
                cancion = Cancion(cancion_nombre, duracion, genero)
                artista.agregar_cancion(cancion)
            else:
                print("Artista no encontrado")

        elif opcion == "3":
            nombre = input("Nombre del artista: ").strip()
            artista = discografia.buscar_artista(nombre)
            if artista:
                album_nombre = input("Nombre del álbum: ").strip()
                anio = int(input("Año de lanzamiento: "))
                album = Album(album_nombre, anio)
                artista.agregar_album(album)

                # Bucle para agregar múltiples canciones al álbum
                while True:
                    cancion_nombre = input("Nombre de la canción del álbum: ").strip()
                    duracion = float(input("Duración en minutos: "))
                    genero = input("Género: ").strip()
                    cancion = Cancion(cancion_nombre, duracion, genero)
                    album.agregar_cancion(cancion)

                    agregar_mas = input("¿Agregar otra canción al álbum? (s/n): ").strip().lower()
                    if agregar_mas != "s":
                        break
            else:
                print("Artista no encontrado")

        elif opcion == "4":
            nombre = input("Nombre del artista: ").strip()
            artista = discografia.buscar_artista(nombre)
            if artista:
                artista.mostrar_discografia()
            else:
                print("Artista no encontrado")

        elif opcion == "5":
            discografia.mostrar_todos_los_artistas()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()