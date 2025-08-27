from inventario import Inventario
from producto import Producto
import os

# Nombre del archivo donde se guardará el inventario
ARCHIVO_INVENTARIO = "inventario_campitos_ecuador.json"


def mostrar_menu():
    """Muestra el menú principal de la aplicación de Campitos Store Ecuador"""
    print("\n" + "=" * 55)
    print("      SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("          CAMPITOS STORE ECUADOR")
    print("=" * 55)
    print("1. Agregar nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de producto")
    print("4. Buscar producto por nombre")
    print("5. Buscar producto por ID")
    print("6. Mostrar todos los productos")
    print("7. Guardar inventario en archivo")
    print("8. Cargar inventario desde archivo")
    print("9. Salir")
    print("=" * 55)


def inicializar_inventario() -> Inventario:
    """
    Inicializa el inventario con productos de la canasta familiar ecuatoriana
    si no existe un archivo previo. Precios en dólares estadounidenses.
    """
    inventario = Inventario()

    # Productos típicos de la canasta familiar ecuatoriana con precios en dólares
    productos_iniciales = [
        (1, "Arroz", 50, 2.50),
        (2, "Fréjol", 40, 3.00),
        (3, "Aceite", 30, 4.50),
        (4, "Azúcar", 45, 1.80),
        (5, "Sal", 35, 1.20),
        (6, "Café", 25, 5.50),
        (7, "Panela", 20, 2.80),
        (8, "Harina de trigo", 30, 2.20),
        (9, "Pasta", 40, 1.50),
        (10, "Atún", 25, 2.00),
        (11, "Leche", 60, 1.20),
        (12, "Huevos (30 unidades)", 100, 4.50),
        (13, "Papa", 70, 1.20),
        (14, "Cebolla", 65, 1.50),
        (15, "Tomate", 55, 1.80),
        (16, "Plátano", 80, 2.00),
        (17, "Yuca", 45, 1.50),
        (18, "Zanahoria", 40, 1.20),
        (19, "Arveja", 35, 2.50),
        (20, "Lenteja", 30, 2.80),
        (21, "Avena", 25, 2.20),
        (22, "Aceituna", 20, 3.50),
        (23, "Queso", 30, 5.00),
        (24, "Mantequilla", 25, 2.80),
        (25, "Galletas", 40, 1.50)
    ]

    # Agregamos los productos iniciales
    for id_prod, nombre, cantidad, precio in productos_iniciales:
        try:
            producto = Producto(id_prod, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        except ValueError as e:
            print(f"Error al crear producto {nombre}: {e}")

    return inventario


def main():
    """
    Función principal que ejecuta el sistema de gestión de inventarios
    para Campitos Store Ecuador con productos de la canasta familiar.
    """
    inventario = Inventario()

    # Intentamos cargar el inventario al iniciar la aplicación
    if inventario.cargar_desde_archivo(ARCHIVO_INVENTARIO):
        print(f"✅ Inventario cargado desde {ARCHIVO_INVENTARIO}")
        print(f"   Total de productos: {len(inventario)}")
    else:
        print("📝 No se encontró un inventario previo. Creando inventario inicial...")
        inventario = inicializar_inventario()
        if inventario.guardar_en_archivo(ARCHIVO_INVENTARIO):
            print(f"✅ Inventario inicial creado con {len(inventario)} productos de la canasta familiar ecuatoriana")
        else:
            print("❌ Error al crear el inventario inicial")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ").strip()

        if opcion == "1":
            # Agregar nuevo producto
            try:
                print("\n➕ AGREGAR NUEVO PRODUCTO")
                print("-" * 30)
                id_producto = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad disponible: "))
                precio = float(input("Ingrese el precio del producto (USD): "))

                # Validamos que el nombre no esté vacío
                if not nombre.strip():
                    print("❌ Error: El nombre del producto no puede estar vacío.")
                    continue

                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)

                if inventario.agregar_producto(nuevo_producto):
                    print("✅ Producto agregado exitosamente!")
                else:
                    print("❌ Error: Ya existe un producto con ese ID.")

            except ValueError as e:
                print(f"❌ Error: {e}")
            except Exception as e:
                print(f"❌ Error inesperado: {e}")

        elif opcion == "2":
            # Eliminar producto por ID
            try:
                print("\n🗑️ ELIMINAR PRODUCTO")
                print("-" * 30)
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))

                # Mostramos información del producto antes de eliminar
                producto = inventario.buscar_por_id(id_producto)
                if producto:
                    print(f"Producto a eliminar: {producto}")
                    confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ").strip().lower()

                    if confirmacion == 's':
                        if inventario.eliminar_producto(id_producto):
                            print("✅ Producto eliminado exitosamente!")
                        else:
                            print("❌ Error al eliminar el producto.")
                    else:
                        print("❌ Eliminación cancelada.")
                else:
                    print("❌ Error: No existe un producto con ese ID.")

            except ValueError:
                print("❌ Error: Ingrese un ID válido (número entero).")

        elif opcion == "3":
            # Actualizar cantidad o precio de producto
            try:
                print("\n🔄 ACTUALIZAR PRODUCTO")
                print("-" * 30)
                id_producto = int(input("Ingrese el ID del producto a actualizar: "))

                # Verificamos que el producto exista
                producto = inventario.buscar_por_id(id_producto)
                if not producto:
                    print("❌ Error: No existe un producto con ese ID.")
                    continue

                print(f"Producto actual: {producto}")

                # Preguntamos qué desea actualizar
                print("\n¿Qué desea actualizar?")
                print("1. Cantidad")
                print("2. Precio (USD)")
                print("3. Ambos")
                sub_opcion = input("Seleccione una opción (1-3): ").strip()

                cantidad = None
                precio = None

                if sub_opcion in ["1", "3"]:
                    try:
                        cantidad = int(input("Ingrese la nueva cantidad: "))
                    except ValueError:
                        print("❌ Error: La cantidad debe ser un número entero.")
                        continue

                if sub_opcion in ["2", "3"]:
                    try:
                        precio = float(input("Ingrese el nuevo precio (USD): "))
                    except ValueError:
                        print("❌ Error: El precio debe ser un número válido.")
                        continue

                if inventario.actualizar_producto(id_producto, cantidad, precio):
                    print("✅ Producto actualizado exitosamente!")
                    producto_actualizado = inventario.buscar_por_id(id_producto)
                    print(f"Producto actualizado: {producto_actualizado}")
                else:
                    print("❌ Error al actualizar el producto.")

            except ValueError:
                print("❌ Error: Asegúrese de ingresar valores numéricos válidos.")

        elif opcion == "4":
            # Buscar producto por nombre
            print("\n🔍 BUSCAR PRODUCTO POR NOMBRE")
            print("-" * 30)
            nombre = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip()

            if not nombre:
                print("❌ Error: Debe ingresar un nombre para buscar.")
            else:
                resultados = inventario.buscar_por_nombre(nombre)

                if resultados:
                    print(f"\n✅ Se encontraron {len(resultados)} producto(s):")
                    for i, producto in enumerate(resultados, 1):
                        print(f"{i}. {producto}")
                else:
                    print("❌ No se encontraron productos con ese nombre.")

        elif opcion == "5":
            # Buscar producto por ID
            try:
                print("\n🔍 BUSCAR PRODUCTO POR ID")
                print("-" * 30)
                id_producto = int(input("Ingrese el ID del producto a buscar: "))

                producto = inventario.buscar_por_id(id_producto)
                if producto:
                    print(f"\n✅ Producto encontrado:")
                    print(producto)
                else:
                    print("❌ No se encontró un producto con ese ID.")

            except ValueError:
                print("❌ Error: Ingrese un ID válido (número entero).")

        elif opcion == "6":
            # Mostrar todos los productos
            print("\n📦 INVENTARIO COMPLETO")
            print("-" * 30)
            productos = inventario.mostrar_todos()

            if productos:
                # Ordenamos los productos por ID para mejor visualización
                productos_ordenados = sorted(productos, key=lambda p: p.id)

                print(f"Total de productos: {len(productos_ordenados)}")
                print("-" * 65)
                for producto in productos_ordenados:
                    print(f"• {producto}")

                # Calculamos el valor total del inventario en dólares
                valor_total = sum(p.cantidad * p.precio for p in productos)
                print("-" * 65)
                print(f"Valor total del inventario: ${valor_total:,.2f} USD")
            else:
                print("📭 El inventario está vacío.")

        elif opcion == "7":
            # Guardar inventario en archivo
            print("\n💾 GUARDAR INVENTARIO")
            print("-" * 30)
            if inventario.guardar_en_archivo(ARCHIVO_INVENTARIO):
                print(f"✅ Inventario guardado exitosamente en {ARCHIVO_INVENTARIO}")
                print(f"   Total de productos guardados: {len(inventario)}")
            else:
                print("❌ Error al guardar el inventario.")

        elif opcion == "8":
            # Cargar inventario desde archivo
            print("\n📂 CARGAR INVENTARIO")
            print("-" * 30)
            confirmacion = input("¿Está seguro? Se perderán los cambios no guardados. (s/n): ").strip().lower()

            if confirmacion == 's':
                if inventario.cargar_desde_archivo(ARCHIVO_INVENTARIO):
                    print(f"✅ Inventario cargado exitosamente desde {ARCHIVO_INVENTARIO}")
                    print(f"   Total de productos cargados: {len(inventario)}")
                else:
                    print("❌ Error: No se pudo cargar el inventario.")
            else:
                print("❌ Carga cancelada.")

        elif opcion == "9":
            # Salir del programa
            print("\n💾 Guardando inventario antes de salir...")
            if inventario.guardar_en_archivo(ARCHIVO_INVENTARIO):
                print(f"✅ Inventario guardado en {ARCHIVO_INVENTARIO}")
            else:
                print("❌ Error al guardar el inventario. Los cambios podrían perderse.")

            print("\n¡Gracias por usar el sistema de gestión de Campitos Store Ecuador! 👋")
            print("¡Vuelve pronto! 🛒")
            break

        else:
            print("❌ Opción no válida. Por favor, seleccione una opción del 1 al 9.")

        # Pausa antes de continuar
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    # Mensaje de bienvenida
    print("=" * 55)
    print("   BIENVENIDO A CAMPITOS STORE ECUADOR")
    print("   Sistema de Gestión de Inventarios")
    print("=" * 55)

    # Ejecutamos la aplicación principal
    main()