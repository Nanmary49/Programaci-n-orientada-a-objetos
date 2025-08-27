import json
import os
from typing import Dict, List, Optional


class Producto:
    """
    Clase que representa un producto en el inventario de Campitos Store Ecuador.
    Cada producto tiene un ID único, nombre, cantidad y precio en dólares.
    """

    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        # Validamos que los valores sean válidos
        if id_producto <= 0:
            raise ValueError("El ID debe ser un número positivo")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos para obtener los atributos (getters)
    @property
    def id(self) -> int:
        """Devuelve el ID único del producto"""
        return self._id

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del producto"""
        return self._nombre

    @property
    def cantidad(self) -> int:
        """Devuelve la cantidad disponible en inventario"""
        return self._cantidad

    @property
    def precio(self) -> float:
        """Devuelve el precio unitario del producto en dólares"""
        return self._precio

    # Métodos para establecer los atributos (setters)
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        """Establece un nuevo nombre para el producto"""
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nuevo_nombre

    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        """Establece una nueva cantidad para el producto"""
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = nueva_cantidad

    @precio.setter
    def precio(self, nuevo_precio: float):
        """Establece un nuevo precio para el producto en dólares"""
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = nuevo_precio

    def to_dict(self) -> Dict:
        """
        Convierte el producto a un diccionario para serialización.
        Útil para guardar en archivo JSON.
        """
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """
        Crea un producto a partir de un diccionario.
        Útil para cargar desde archivo JSON.
        """
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])

    def __str__(self) -> str:
        """
        Representación en string del producto.
        Formato: ID: 1, Producto: Arroz, Cantidad: 50, Precio: $2.50
        """
        return f"ID: {self._id}, Producto: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"

    def __repr__(self) -> str:
        """Representación oficial del objeto para debugging"""
        return f"Producto(id={self._id}, nombre='{self._nombre}', cantidad={self._cantidad}, precio={self._precio})"