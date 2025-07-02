# Clase base: Persona
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # atributo encapsulado (convención con "_")
        self._edad = edad      # atributo encapsulado

    # Método para mostrar información (puede ser sobrescrito)
    def mostrar_informacion(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}")

    # Método getter para nombre
    def get_nombre(self):
        return self._nombre

    # Método setter para nombre
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

# Clase derivada: Estudiante (hereda de Persona)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.__carrera = carrera        # atributo privado con doble guión bajo (__)

    # Método sobrescrito (polimorfismo)
    def mostrar_informacion(self):
        print(f"Estudiante: {self._nombre}, Edad: {self._edad}, Carrera: {self.__carrera}")

    # Método específico de la clase derivada
    def estudiar(self):
        print(f"{self._nombre} está estudiando la carrera de {self.__carrera}.")

# Función polimórfica
def presentar(persona):
    persona.mostrar_informacion()

# Crear instancias y mostrar funcionalidad
persona1 = Persona("Luis", 40)
estudiante1 = Estudiante("Ana", 22, "Ingeniería de Sistemas")

# Usar métodos
print("=== Información de persona ===")
persona1.mostrar_informacion()

print("\n=== Información de estudiante ===")
estudiante1.mostrar_informacion()

# Usar métodos get/set
print("\n=== Encapsulamiento (get/set) ===")
print("Nombre actual:", estudiante1.get_nombre())
estudiante1.set_nombre("Ana María")
print("Nuevo nombre:", estudiante1.get_nombre())

# Método específico de la clase Estudiante
print("\n=== Método exclusivo de Estudiante ===")
estudiante1.estudiar()

# Demostración de polimorfismo con función presentar
print("\n=== Polimorfismo con función ===")
presentar(persona1)      # Llama a mostrar_informacion de Persona
presentar(estudiante1)   # Llama a mostrar_informacion de Estudiante (sobrescrito)
