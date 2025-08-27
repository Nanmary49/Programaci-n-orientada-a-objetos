from producto import Producto
import json
import os
from typing import Dict, List, Optional


class Inventario:
    """
    Clase que gestiona el inventario de Campitos Store Ecuador.
    Utiliza un diccionario para almacenar los productos, permitiendo operaciones eficientes.
    """

    def __init__(self):
        # Usamos un diccionario para acceso rápido por ID (O(1) para búsquedas por ID)
        self._productos: Dict[int, Producto] = {}

    def agregar_producto(self, producto: Producto) -> bool:
        """
        Agrega un nuevo producto al inventario.

        Args:
            producto: Instancia de Producto a agregar

        Returns:
            True si se agregó correctamente, False si el ID ya existe.
        """
        if producto.id in self._productos:
            return False  # El ID ya existe

        self._productos[producto.id] = producto
        return True

    def eliminar_producto(self, id_producto: int) -> bool:
        """
        Elimina un producto del inventario por su ID.

        Args:
            id_producto: ID del producto a eliminar

        Returns:
            True si se eliminó correctamente, False si el ID no existe.
        """
        if id_producto in self._productos:
            del self._productos[id_producto]
            return True
        return False

    def actualizar_producto(self, id_producto: int, cantidad: Optional[int] = None,
                            precio: Optional[float] = None) -> bool:
        """
        Actualiza la cantidad y/o precio de un producto existente.

        Args:
            id_producto: ID del producto a actualizar
            cantidad: Nueva cantidad (opcional)
            precio: Nuevo precio (opcional)

        Returns:
            True si se actualizó correctamente, False si el ID no existe.
        """
        if id_producto not in self._productos:
            return False

        producto = self._productos[id_producto]
        if cantidad is not None:
            producto.cantidad = cantidad
        if precio is not None:
            producto.precio = precio

        return True

    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        """
        Busca productos por nombre (búsqueda parcial case-insensitive).

        Args:
            nombre: Texto a buscar en los nombres de productos

        Returns:
            Lista de productos que coinciden con el nombre.
        """
        resultados = []
        nombre_lower = nombre.lower()

        # Recorremos todos los productos para buscar coincidencias
        for producto in self._productos.values():
            if nombre_lower in producto.nombre.lower():
                resultados.append(producto)

        return resultados

    def buscar_por_id(self, id_producto: int) -> Optional[Producto]:
        """
        Busca un producto por su ID.

        Args:
            id_producto: ID del producto a buscar

        Returns:
            El producto si existe, None si no existe.
        """
        return self._productos.get(id_producto)

    def mostrar_todos(self) -> List[Producto]:
        """
        Obtiene todos los productos del inventario.

        Returns:
            Lista con todos los productos del inventario.
        """
        return list(self._productos.values())

    def cantidad_productos(self) -> int:
        """
        Devuelve la cantidad total de productos en el inventario.

        Returns:
            Número de productos en el inventario.
        """
        return len(self._productos)

    def guardar_en_archivo(self, nombre_archivo: str) -> bool:
        """
        Guarda el inventario completo en un archivo JSON.

        Args:
            nombre_archivo: Ruta del archivo donde guardar

        Returns:
            True si se guardó correctamente, False en caso de error.
        """
        try:
            # Convertimos todos los productos a diccionarios
            datos = [producto.to_dict() for producto in self._productos.values()]

            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)

            return True
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")
            return False

    def cargar_desde_archivo(self, nombre_archivo: str) -> bool:
        """
        Carga el inventario desde un archivo JSON.

        Args:
            nombre_archivo: Ruta del archivo desde donde cargar

        Returns:
            True si se cargó correctamente, False en caso de error.
        """
        try:
            # Verificamos si el archivo existe
            if not os.path.exists(nombre_archivo):
                return False

            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)

            # Limpiamos el inventario actual y cargamos los nuevos datos
            self._productos.clear()
            for item in datos:
                producto = Producto.from_dict(item)
                self._productos[producto.id] = producto

            return True
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")
            return False

    def __len__(self) -> int:
        """Devuelve la cantidad de productos en el inventario"""
        return len(self._productos)

    def __contains__(self, id_producto: int) -> bool:
        """Verifica si un producto existe en el inventario por ID"""
        return id_producto in self._productos