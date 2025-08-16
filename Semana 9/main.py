from inventario import Inventario
from producto import Producto

def cargar_productos_iniciales(inventario):
    """
    Agrega productos de ejemplo para que el inventario no esté vacío.
    """
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
    for p in productos_iniciales:
        inventario.añadir_producto(p)

def menu():
    inventario = Inventario("Comercial Nancy Campos")
    cargar_productos_iniciales(inventario)

    while True:
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
                id_producto = int(input("Ingrese ID único: "))
                nombre = input("Ingrese nombre: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                nuevo = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo)
            except ValueError:
                print("❌ Error: Datos inválidos.")

        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("❌ Error: ID inválido.")

        elif opcion == "3":
            try:
                id_producto = int(input("Ingrese ID del producto a actualizar: "))
                nueva_cantidad = input("Nueva cantidad (ENTER para omitir): ")
                nuevo_precio = input("Nuevo precio (ENTER para omitir): ")

                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("❌ Error: Datos inválidos.")

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("👋 Gracias por usar el sistema de inventario. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
