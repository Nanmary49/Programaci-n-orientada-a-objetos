import sys
import os
import json
from json.decoder import JSONDecodeError

import sys
import os
import json
from json.decoder import JSONDecodeError

import sys
import os
import json
import sys
import os
import json
from json.decoder import JSONDecodeError

import sys
import os
import json
from json.decoder import JSONDecodeError

import sys
import os
import json
from json.decoder import JSONDecodeError


# === PARTE 1: DEFINICIÓN DE LA CLASE PRODUCTO ===
# -----------------------------------------------------------------------------
# Esta clase modela un solo producto y sus propiedades.
# Se ha añadido el método to_dict() para la serialización de datos.

class Producto:
    """
    Clase que representa un producto en el inventario.
    Cada producto tiene un ID único, un nombre, cantidad y precio.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto."""
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters (métodos para obtener valores)
    def get_id(self):
        """Devuelve el ID único del producto."""
        return self.id_producto

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self.nombre

    def get_cantidad(self):
        """Devuelve la cantidad en stock del producto."""
        return self.cantidad

    def get_precio(self):
        """Devuelve el precio del producto."""
        return self.precio

    # Setters (métodos para establecer o modificar valores)
    def set_id(self, id_producto):
        """Establece un nuevo ID para el producto."""
        self.id_producto = id_producto

    def set_nombre(self, nombre):
        """Establece un nuevo nombre para el producto."""
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        """Establece una nueva cantidad en stock."""
        self.cantidad = cantidad

    def set_precio(self, precio):
        """Establece un nuevo precio."""
        self.precio = precio

    # Métodos especiales para la funcionalidad del objeto
    def __str__(self):
        """
        Método de representación en cadena.
        Permite que el objeto sea impreso de forma legible (ej. print(producto)).
        """
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def to_dict(self):
        """
        Convierte el objeto Producto a un diccionario de Python.
        Este proceso se llama "serialización". Es necesario porque el módulo `json`
        no puede escribir directamente objetos de clases personalizadas en un archivo.
        """
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


# === PARTE 2: DEFINICIÓN DE LA CLASE INVENTARIO ===
# -----------------------------------------------------------------------------
# Esta clase administra una colección de objetos Producto.
# Se ha modificado para manejar la lectura y escritura de archivos y excepciones.

class Inventario:
    """
    Clase que administra el inventario de una tienda.
    Ahora incluye persistencia en archivos y robusto manejo de excepciones.
    """

    def __init__(self, nombre_tienda, nombre_archivo="inventario.txt"):
        """
        Constructor de la clase Inventario.
        Al instanciarse, intenta cargar el estado del inventario desde un archivo.
        """
        self.nombre_tienda = nombre_tienda
        self.nombre_archivo = nombre_archivo
        self.productos = []
        # Llamada inicial para cargar el inventario guardado.
        self.cargar_inventario()

    def _get_productos_dict(self):
        """
        Método auxiliar para obtener la lista de productos como diccionarios.
        Es una abstracción para mejorar la legibilidad del código.
        """
        return [p.to_dict() for p in self.productos]

    def _reconstruir_productos(self, lista_json):
        """
        Método auxiliar para reconstruir objetos Producto a partir de una lista de diccionarios.
        Es la contraparte de to_dict(), un proceso llamado "deserialización".
        """
        return [Producto(p['id'], p['nombre'], p['cantidad'], p['precio']) for p in lista_json]

    def guardar_inventario(self):
        """
        Guarda el estado actual del inventario en el archivo `inventario.txt`.
        Implementa un robusto manejo de excepciones para fallas de escritura.
        """
        try:
            with open(self.nombre_archivo, "w", encoding="utf-8") as f:
                # Serializa la lista de objetos Producto a JSON. `indent=4` mejora la legibilidad.
                json.dump(self._get_productos_dict(), f, indent=4)
            print(f"✅ Inventario guardado en '{self.nombre_archivo}' correctamente.")
        except PermissionError:
            # Captura el error si el programa no tiene permisos de escritura en la carpeta.
            print(f"❌ Error de Permiso: No se puede escribir en '{self.nombre_archivo}'.")
        except Exception as e:
            # Captura cualquier otro error inesperado durante el proceso.
            print(f"❌ Error inesperado al guardar el archivo: {e}")

    def cargar_inventario(self):
        """
        Carga el inventario desde el archivo `inventario.txt` al iniciar el programa.
        Maneja diferentes escenarios de errores de lectura.
        """
        # 1. Verificar si el archivo existe para evitar FileNotFoundError inicial.
        if not os.path.exists(self.nombre_archivo):
            print(f"📦 El archivo '{self.nombre_archivo}' no existe. Se creará uno nuevo.")
            # Si el archivo no existe, simplemente se continúa con una lista de productos vacía.
            return

        try:
            with open(self.nombre_archivo, "r", encoding="utf-8") as f:
                # 2. Deserializa el contenido del archivo JSON a una lista de diccionarios.
                productos_json = json.load(f)
                # 3. Reconstruye los objetos Producto a partir de la lista de diccionarios.
                self.productos = self._reconstruir_productos(productos_json)
            print(f"✅ Inventario cargado desde '{self.nombre_archivo}' correctamente.")
        except FileNotFoundError:
            # Captura el caso, aunque ya se maneja con os.path.exists().
            print(f"❌ Error: El archivo '{self.nombre_archivo}' no fue encontrado.")
        except JSONDecodeError:
            # Captura si el archivo existe pero su contenido no es un JSON válido o está vacío.
            print(
                f"❌ Error de Formato: El archivo '{self.nombre_archivo}' está corrupto o vacío. Se reiniciará el inventario.")
            self.productos = []  # Restaura a un estado vacío para evitar que el programa falle.
        except PermissionError:
            # Captura si el programa no tiene permisos de lectura para el archivo.
            print(f"❌ Error de Permiso: No se puede leer el archivo '{self.nombre_archivo}'.")
        except Exception as e:
            # Captura cualquier otro error durante la carga.
            print(f"❌ Error inesperado al cargar el archivo: {e}")

    def añadir_producto(self, producto):
        """Añade un nuevo producto y luego persiste el cambio en el archivo."""
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print(f"✅ Producto '{producto.get_nombre()}' añadido correctamente.")
        # Llama a guardar_inventario() para que el cambio sea permanente.
        self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID y guarda el cambio."""
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(f"🗑️ Producto con ID {id_producto} eliminado correctamente.")
                # Llama a guardar_inventario() para que el cambio sea permanente.
                self.guardar_inventario()
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad y/o el precio de un producto y guarda el cambio."""
        for p in self.productos:
            if p.get_id() == id_producto:
                # Usa los setters de la clase Producto para aplicar los cambios.
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("🔄 Producto actualizado correctamente.")
                # Llama a guardar_inventario() para que el cambio sea permanente.
                self.guardar_inventario()
                return
        print("❌ Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre de forma insensible a mayúsculas/minúsculas."""
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print(f"🔎 Resultados de búsqueda para '{nombre}':")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        """Muestra una lista completa de todos los productos en el inventario."""
        if not self.productos:
            print(f"📦 El inventario de {self.nombre_tienda} está vacío.")
        else:
            print(f"📋 Productos en inventario de {self.nombre_tienda}:")
            for p in self.productos:
                print(p)


# === PARTE 3: LÓGICA DEL MENÚ Y EJECUCIÓN ===
# -----------------------------------------------------------------------------
# Esta sección contiene la interfaz de usuario para interactuar con el inventario.

def cargar_productos_iniciales(inventario):
    """
    Función que añade productos de ejemplo solo si el inventario está vacío.
    Esto evita duplicar productos cada vez que se reinicia el programa.
    """
    # La condición verifica si la lista de productos está vacía después de intentar cargar el archivo.
    if not inventario.productos:
        print("\n--- El inventario está vacío. Cargando productos de ejemplo. ---")
        productos_iniciales = [
            Producto(1, "Leche", 10, 1.50),
            Producto(2, "Pan", 25, 0.30),
            Producto(3, "Arroz", 50, 0.90),
            Producto(4, "Azúcar", 40, 1.20),
            Producto(5, "Aceite", 15, 3.50),
            Producto(6, "Huevos", 60, 0.12),
            Producto(7, "Queso", 20, 2.80),
            Producto(8, "Café", 30, 4.50),
            Producto(9, "Fideos", 35, 1.10),
            Producto(10, "Galletas", 45, 0.80),
            Producto(11, "Agua", 100, 0.50),
            Producto(12, "Jugo", 70, 1.75)
        ]
        # Bucle para añadir cada producto de la lista inicial.
        for p in productos_iniciales:
            inventario.añadir_producto(p)


def menu():
    """
    Función principal que ejecuta el bucle del menú interactivo del inventario.
    """
    # Se crea una instancia de la clase Inventario, que automáticamente intenta cargar los datos.
    inventario = Inventario("Comercial Nancy Campos")
    # Luego, se añaden productos iniciales si el archivo estaba vacío o no existía.
    cargar_productos_iniciales(inventario)

    while True:
        # Menú principal y opciones
        print(f"\n===== INVENTARIO DE {inventario.nombre_tienda.upper()} =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                # Se pide la entrada del usuario y se convierten a los tipos de datos correctos.
                id_producto = int(input("Ingrese ID único: "))
                nombre = input("Ingrese nombre: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                nuevo = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo)
            except ValueError:
                # Captura si el usuario ingresa un valor que no es un número.
                print("❌ Error: Datos inválidos. Asegúrese de ingresar números para ID, cantidad y precio.")

        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("❌ Error: ID inválido. Debe ingresar un número entero.")

        elif opcion == "3":
            try:
                id_producto = int(input("Ingrese ID del producto a actualizar: "))
                nueva_cantidad_str = input("Nueva cantidad (ENTER para omitir): ")
                nuevo_precio_str = input("Nuevo precio (ENTER para omitir): ")

                # Se maneja la entrada opcional del usuario.
                nueva_cantidad = int(nueva_cantidad_str) if nueva_cantidad_str else None
                nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("❌ Error: Datos inválidos. Asegúrese de que la cantidad y el precio sean números.")

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("👋 Gracias por usar el sistema de inventario. ¡Hasta luego!")
            # sys.exit() termina la ejecución del programa de forma limpia.
            sys.exit()
        else:
            print("❌ Opción inválida. Por favor, intente de nuevo.")


# Punto de entrada del programa.
if __name__ == "__main__":
    menu()