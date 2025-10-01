from dataclasses import dataclass, field, asdict
import operaciones
from typing import List

@dataclass(frozen=True)
class Persona:
    __nombre: str = field(repr=False)
    edad: int = field(default=35)

    @property
    def retornar_edad_por_2(self) -> int:
        return self.edad * 2

@dataclass
class Puesto:
    nombre: str
    persona: Persona

@dataclass
class Grupo:
    personas: List[Persona] = field(default_factory=list)

class Persona2:
    def __init__(self, nombre, edad=35):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Juan")
persona2 = Persona2("Camila")

print(persona1.retornar_edad_por_2)

puesto1 = Puesto("Desarrollador", persona1)

grupo1 = Grupo()
grupo1.personas.append(persona1)
grupo1.personas.append(persona2)

print(grupo1)

print(operaciones.suma(persona1.edad, persona2.edad))

print(puesto1)

print(asdict(persona1))

if persona1 == persona2:
    print("Son iguales")
else:
    print("No son iguales")