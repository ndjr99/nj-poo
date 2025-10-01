class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y mi correo es {self.correo}")

class Empleado(Persona):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo)
        self.salario = salario

    def calcular_bono(self):
        pass

class Desarrollador(Empleado):
    def __init__(self, nombre, correo, salario, lenguaje_principal):
        super().__init__(nombre, correo, salario)
        self.lenguaje = lenguaje_principal

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, mi correo es {self.correo} y soy desarrollador de {self.lenguaje}")

    def calcular_bono(self, empresa):
        bono = self.salario * 0.10
        tareas_asignadas = 0
        for proyecto in empresa.proyectos:
            for tarea in proyecto.tareas:
                if tarea.asignado_a == self:
                    tareas_asignadas += 1
        if tareas_asignadas > 5:
            bono += self.salario * 0.01
        return bono
    
class Analista(Empleado):
    def __init__(self, nombre, correo, salario, seniority):
        super().__init__(nombre, correo, salario)
        self.seniority = seniority

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, mi correo es {self.correo} y soy analista {self.seniority}")

    def calcular_bono(self):
        bono = self.salario * 0.08
        if self.seniority.lower() == "senior":
            bono += self.salario * 0.03
        return bono
    
class Gerente(Empleado):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo, salario)
        self.empleados_a_cargo = []

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, mi correo es {self.correo} y soy gerente")

    def agregar_empleado(self, e):
        if e == self:
            print("No se puede agregar a sí mismo como empleado de su equipo.")
            return
        existe = False
        for empleado in self.empleados_a_cargo:
            if empleado == e:
                print(f"El empleado {e.nombre} ya está en el equipo del gerente {self.nombre}.")
                existe = True
                break
        if existe == False:
            self.empleados_a_cargo.append(e)
            print(f"Empleado {e.nombre} agregado al equipo del gerente {self.nombre}.")
            return
            
    def remover_empleado(self, e):
        existe = False
        for eempleado in self.empleados_a_cargo:
            if eempleado == e:
                self.empleados_a_cargo.remove(e)
                print(f"Empleado {e.nombre} removido del equipo del gerente {self.nombre}.")
                existe = True
                break
        if existe == False:
            print(f"El empleado {e.nombre} no está en el equipo del gerente {self.nombre}.")
            
    def listar_equipo(self):
        print(f"Equipo del gerente {self.nombre}:")
        if len(self.empleados_a_cargo) == 0:
            print("No hay empleados a cargo.")
            return
        for e in self.empleados_a_cargo:
            print(e.nombre)

class Tarea:
    def __init__(self, id, descripcion, horas_estimadas):
        self.id = id
        self.descripcion = descripcion
        self.horas_estimadas = horas_estimadas
        self.asignado_a = None
        
class Proyecto:
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.tareas = []
        self.tarea_id = 0

    def agregar_tarea(self, descripcion, horas_estimadas):
        if horas_estimadas < 0:
            print(f"No se puede agregar la tarea {descripcion} porque tiene horas negativas.")
            return
        else:
            self.tarea_id += 1
            tarea = Tarea(self.tarea_id, descripcion, horas_estimadas)
            self.tareas.append(tarea)
            print(f"Tarea {descripcion} agregada al proyecto {self.nombre} con ID {tarea.id}.")

    def asignar_empleado(self, tarea_id, empleado):
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                tarea.asignado_a = empleado
                print(f"Tarea {tarea.descripcion} asignada a {empleado.nombre}.")
                return
        else:
            print(f"No se encontró la tarea con ID {tarea_id}.")

class Empresa:
    def __init__(self):
        self.empleados = []
        self.proyectos = []

    def agregar_empleado(self, e):
        existe = False
        for empleado in self.empleados:
            if empleado == e:
                print(f"El empleado {e.nombre} ya está en la empresa.")
                existe = True
                break
        if existe == False:
            self.empleados.append(e)
            print(f"Empleado {e.nombre} agregado a la empresa.")

    def crear_proyecto(self, p):
        existe = False
        for proyecto in self.proyectos:
            if proyecto == p:
                print(f"El proyecto {p.nombre} ya está en la empresa.")
                existe = True
                break
        if existe == False:
            self.proyectos.append(p)
            print(f"Proyecto {p.nombre} agregado a la empresa.")

    def eliminar_proyecto(self, p):
        existe = False
        for proyecto in self.proyectos:
            if proyecto == p:
                self.proyectos.remove(p)
                print(f"Proyecto {p.nombre} eliminado de la empresa.")
                existe = True
                break
        if existe == False:
            print(f"El proyecto {p.nombre} no está en la empresa.")

    def asignar_empleado_a_proyecto(self, proyecto, tarea_id, empleado):
        existe = False
        for p in self.proyectos:
            if p == proyecto:
                p.asignar_empleado(tarea_id, empleado)
                existe = True
                break
        if existe == False:
            print(f"El proyecto {proyecto.nombre} no está en la empresa.")

#Escenario de ejemplo

#Se crea la empresa
empresa = Empresa()

#Se crean y se agregan los empleados a la empresa
desarrollador1 = Desarrollador("Juan", "juan@gmail.com", 2500, "Python")
empresa.agregar_empleado(desarrollador1)
desarrollador2 = Desarrollador("Ana", "ana@gmail.com", 3000, "Java")
empresa.agregar_empleado(desarrollador2)
analista1 = Analista("Luis", "luis@gmail.com", 3500, "Senior")
empresa.agregar_empleado(analista1)
gerente1 = Gerente("Carlos", "carlos@gmail.com", 5000)
empresa.agregar_empleado(gerente1)
gerente2 = Gerente("Maria", "maria@gmail.com", 5200)
empresa.agregar_empleado(gerente2)
empresa.agregar_empleado(desarrollador1) #Se intenta agregar un empleado que ya existe

print()

#Se presentan los empleados
desarrollador1.presentarse()
desarrollador2.presentarse()
analista1.presentarse()
gerente1.presentarse()
gerente2.presentarse()

print()

#Se agregan empleados al equipo de un gerente
gerente1.agregar_empleado(desarrollador1)
gerente1.agregar_empleado(analista1)
gerente1.agregar_empleado(analista1) #Se intenta agregar un empleado que ya está en el equipo)
gerente1.agregar_empleado(gerente1) #Se intenta agregar a sí mismo
gerente1.listar_equipo() #Se lista el equipo del gerente
gerente2.listar_equipo() #Se lista el equipo de un gerente sin empleados

print()

#Se remueve un empleado del equipo de un gerente
gerente1.remover_empleado(analista1)
gerente1.remover_empleado(desarrollador2) #Se intenta remover un empleado que no está en el equipo
gerente1.listar_equipo()

print()

#Se crean y se agregan los proyectos a la empresa
proyecto1 = Proyecto("Sistema Ventas", 10000)
empresa.crear_proyecto(proyecto1)
empresa.crear_proyecto(proyecto1) #Se intenta agregar un proyecto que ya existe

print()

#Se agregan tareas a un proyecto
proyecto1.agregar_tarea("Diseño de la base de datos", 20)
proyecto1.agregar_tarea("Desarrollo", 50)
proyecto1.agregar_tarea("Pruebas", -10) #Se intenta agregar una tarea con horas negativas

print()

#Se asignan empleados a tareas de un proyecto
empresa.asignar_empleado_a_proyecto(proyecto1, 1, analista1)
empresa.asignar_empleado_a_proyecto(proyecto1, 2, desarrollador1)
empresa.asignar_empleado_a_proyecto(proyecto1, 4, desarrollador2) #Se intenta asignar una tarea que no existe

print()

#Se elimina un proyecto de la empresa
empresa.eliminar_proyecto(proyecto1)

print()

#Se calcula el bono de los empleados
print(f"Bono de {desarrollador1.nombre}: {desarrollador1.calcular_bono(empresa)}")
print(f"Bono de {desarrollador2.nombre}: {desarrollador2.calcular_bono(empresa)}")
print(f"Bono de {analista1.nombre}: {analista1.calcular_bono()}")