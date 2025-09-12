class Persona:
    def __init__(self, nombre, cedula, ti):
        self.nombre = nombre
        self.__cedula = cedula
        self.__ti = ti
    
    def obtener_documento(self):
        if self.__cedula is not None:
            return self.__cedula
        else:
            return self.__ti

Persona1 = Persona("Juan", 1111, None)
Persona2 = Persona("Maria", 2222, None)
niño1 = Persona("Isaac", None, 3333)

print("El nombre de la primera persona es", Persona1.nombre)
print("El documento de la primera persona es", Persona1.obtener_documento())

print("El nombre de la segunda persona es", niño1.nombre)
print("El documento de la segunda persona es", niño1.obtener_documento())