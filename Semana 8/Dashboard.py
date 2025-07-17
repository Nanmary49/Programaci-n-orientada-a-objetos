import os

# FUNCIÓN: Muestra el contenido de un archivo de Python en consola
def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("❌ El archivo no se encontró.")
    except Exception as e:
        print(f"⚠️ Ocurrió un error al leer el archivo: {e}")

# FUNCIÓN: Muestra el menú principal con opciones para ver cada script
def mostrar_menu():
    ruta_base = os.path.dirname(__file__)  # Ruta base del archivo actual

    # CAMBIO PERSONAL: Agregué opciones por unidad con rutas a mis scripts
    opciones = {
        '1': 'UNIDAD 1/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'UNIDAD 2/2.1.1. clase_ejemplo.py',
        '3': 'UNIDAD 3/3.2.1. herencia_ejemplo.py',
        '4': 'UNIDAD 4/4.1.1. encapsulamiento.py'
    }

    while True:
        print("\n" + "="*50)
        print("    DASHBOARD DE PROGRAMACIÓN ORIENTADA A OBJETOS")
        print("="*50)

        # Muestra las opciones disponibles
        for key in opciones:
            print(f"{key} - Ver: {opciones[key]}")
        print("0 - Salir")

        eleccion = input("\nElige un número para ver el código o '0' para salir: ")
        if eleccion == '0':
            print("👋 Gracias por usar el dashboard. ¡Hasta pronto!")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("❗ Opción no válida. Intenta de nuevo.")

# Ejecutar el dashboard solo si se corre directamente
if __name__ == "__main__":
    mostrar_menu()
# =====================================================
# REFERENCIA: Códigos de ejemplo de cada unidad
# =====================================================

# --- UNIDAD 1: Técnicas de Programación ---
# Archivo: 1.2.1. Ejemplo Tecnicas de Programacion.py
"""
def saludar(nombre):
    print(f"Hola, {nombre}, bienvenida a Programación Orientada a Objetos.")

saludar("Nancy")
"""

# --- UNIDAD 2: Clases ---
# Archivo: 2.1.1. clase_ejemplo.py
"""
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

alumna = Estudiante("Nancy", 49)
alumna.presentarse()
"""

# --- UNIDAD 3: Herencia ---
# Archivo: 3.2.1. herencia_ejemplo.py
"""
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

class Alumna(Persona):
    def estudiar(self):
        print(f"{self.nombre} está estudiando POO.")

nancy = Alumna("Nancy")
nancy.saludar()
nancy.estudiar()
"""

# --- UNIDAD 4: Encapsulamiento ---
# Archivo: 4.1.1. encapsulamiento.py
"""
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def ver_saldo(self):
        print(f"Tu saldo es: ${self.__saldo}")

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso de ${monto}")

cuenta = CuentaBancaria(100)
cuenta.ver_saldo()
cuenta.depositar(50)
cuenta.ver_saldo()
"""
