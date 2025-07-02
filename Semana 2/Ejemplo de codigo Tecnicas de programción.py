from abc import ABC, abstractmethod

# ------------------------
# ABSTRACCIÓN
# ------------------------
# Creamos una clase abstracta llamada Animal que define una interfaz genérica para todos los animales.

class Animal(ABC):
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre  # Encapsulación: atributo protegido
        self._edad = edad

    @abstractmethod
    def hacer_sonido(self):
        """Método abstracto que debe implementarse en las subclases"""
        pass

    def describir(self):
        """Método común para todos los animales"""
        return f"{self._nombre} tiene {self._edad} años."

# ------------------------
# HERENCIA
# ------------------------
# Las siguientes clases heredan de la clase Animal

class Perro(Animal):
    def __init__(self, nombre: str, edad: int, raza: str):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self._raza = raza  # Encapsulación

    # POLIMORFISMO: redefinimos el método hacer_sonido
    def hacer_sonido(self):
        return "¡Guau!"

    def describir(self):
        # POLIMORFISMO: sobrescribimos el método describir
        return f"{self._nombre} es un perro de raza {self._raza} y tiene {self._edad} años."

class Gato(Animal):
    def __init__(self, nombre: str, edad: int, color: str):
        super().__init__(nombre, edad)
        self._color = color

    def hacer_sonido(self):
        return "¡Miau!"

    def describir(self):
        return f"{self._nombre} es un gato de color {self._color} y tiene {self._edad} años."

# ------------------------
# ENCAPSULACIÓN: Getters y Setters
# ------------------------

class Cuidador:
    def __init__(self, nombre: str):
        self.__nombre = nombre  # Atributo privado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre: str):
        if nuevo_nombre:  # validamos que no esté vacío
            self.__nombre = nuevo_nombre
        else:
            print("Nombre no válido")

# ------------------------
# DEMOSTRACIÓN DEL FUNCIONAMIENTO
# ------------------------

def main():
    # Instancias de animales
    perro1 = Perro("Max", 5, "Labrador")
    gato1 = Gato("Michi", 3, "Blanco")

    # Lista de animales: uso de polimorfismo
    animales = [perro1, gato1]

    for animal in animales:
        print(animal.describir())        # Polimorfismo: cada animal responde a su forma
        print(f"Sonido: {animal.hacer_sonido()}")
        print("-------------")

    # Cuidador
    cuidador = Cuidador("Carlos")
    print(f"Cuidador: {cuidador.get_nombre()}")

    # Modificando nombre con setter
    cuidador.set_nombre("Ana")
    print(f"Nuevo cuidador: {cuidador.get_nombre()}")

if __name__ == "__main__":
    main()
# Corrección el comit anterior decia tarea semana 5 y es semana 2
