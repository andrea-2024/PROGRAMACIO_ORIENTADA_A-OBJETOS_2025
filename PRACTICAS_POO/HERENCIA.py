# Clase base
class MiembroDeFamilia:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Clase derivada para el padre
class Padre(MiembroDeFamilia):
    def __init__(self, nombre, edad, ocupacion):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.ocupacion = ocupacion

    def presentarse(self):
        super().presentarse()
        print(f"Soy el padre y trabajo como {self.ocupacion}.")

# Clase derivada para la madre
class Madre(MiembroDeFamilia):
    def __init__(self, nombre, edad, profesion):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.profesion = profesion

    def presentarse(self):
        super().presentarse()
        print(f"Soy la madre y mi profesión es {self.profesion}.")

# Clase derivada para el hijo
class Hijo(MiembroDeFamilia):
    def __init__(self, nombre, edad, escuela):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.escuela = escuela

    def presentarse(self):
        super().presentarse()
        print(f"Soy el hijo y estudio en {self.escuela}.")

# Crear objetos de las clases derivadas
padre = Padre("Carlos", 40, "Ingeniero")
madre = Madre("Ana", 38, "Doctora")
hijo = Hijo("Luis", 15, "Escuela Secundaria El Sol")

# Llamar al método presentarse
padre.presentarse()
# Salida:
# Hola, soy Carlos y tengo 40 años.
# Soy el padre y trabajo como Ingeniero.

madre.presentarse()
# Salida:
# Hola, soy Ana y tengo 38 años.
# Soy la madre y mi profesión es Doctora.

hijo.presentarse()
# Salida:
# Hola, soy Luis y tengo 15 años.
# Soy el hijo y estudio en Escuela Secundaria El Sol.
