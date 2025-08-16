from producto import Producto

class Inventario:
    """
    Clase que administra el inventario de una tienda.
    """

    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def añadir_producto(self, producto):
        # Evitar IDs duplicados
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print(f"✅ Producto '{producto.get_nombre()}' añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(f"🗑️ Producto con ID {id_producto} eliminado correctamente.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("🔄 Producto actualizado correctamente.")
                return
        print("❌ Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print(f"🔎 Resultados de búsqueda para '{nombre}':")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print(f"📦 El inventario de {self.nombre_tienda} está vacío.")
        else:
            print(f"📋 Productos en inventario de {self.nombre_tienda}:")
            for p in self.productos:
                print(p)
