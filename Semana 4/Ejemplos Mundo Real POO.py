# Clase que representa una película en el cine
class Pelicula:
    def __init__(self, titulo, duracion, clasificacion):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.asientos_disponibles = 20  # Por defecto 20 asientos

    # Muestra la información de la película
    def mostrar_info(self, index=None):
        if index is not None:
            print(f"{index}. 🎥 {self.titulo} | {self.duracion} min | {self.clasificacion} | Asientos: {self.asientos_disponibles}")
        else:
            print(f"🎥 {self.titulo} | {self.duracion} min | {self.clasificacion} | Asientos: {self.asientos_disponibles}")

    # Resta asientos si hay disponibilidad
    def reservar_asiento(self, cantidad):
        if cantidad <= self.asientos_disponibles:
            self.asientos_disponibles -= cantidad
            return True
        return False


# Clase que representa al cliente que compra boletos
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.boletos_reservados = []

    # Realiza la reserva de boletos para una película
    def reservar(self, pelicula, cantidad):
        if pelicula.reservar_asiento(cantidad):
            self.boletos_reservados.append((pelicula, cantidad))
            print(f"\n✅ {cantidad} boleto(s) reservados para '{pelicula.titulo}'.\n")
            self._guardar_en_archivo(pelicula, cantidad)  # Guarda en archivo
        else:
            print("\n❌ No hay suficientes asientos disponibles.\n")

    # Muestra las reservas del cliente
    def mostrar_reservas(self):
        print(f"\n🎟️ Reservas de {self.nombre}:")
        if not self.boletos_reservados:
            print("Aún no tienes reservas.")
        for pelicula, cantidad in self.boletos_reservados:
            print(f"- {cantidad} x {pelicula.titulo}")
        print()

    # Guarda los datos en un archivo de texto
    def _guardar_en_archivo(self, pelicula, cantidad):
        with open("reservas.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Cliente: {self.nombre}\n")
            archivo.write(f"Pelicula: {pelicula.titulo}\n")
            archivo.write(f"Cantidad de boletos: {cantidad}\n")
            archivo.write(f"Asientos restantes: {pelicula.asientos_disponibles}\n")
            archivo.write("-" * 40 + "\n")


# Clase que representa el cine con su cartelera
class Cine:
    def __init__(self):
        self.funciones = []

    # Agrega una película al cine
    def agregar_funcion(self, pelicula):
        self.funciones.append(pelicula)

    # Muestra todas las películas disponibles
    def mostrar_cartelera(self):
        print("\n📅 Cartelera actual del cine:")
        for idx, pelicula in enumerate(self.funciones, 1):
            pelicula.mostrar_info(index=idx)
        print()


# Función para mostrar el menú del sistema
def mostrar_menu():
    print("🎬 Bienvenido al Cine Interactivo")
    print("1. Ver cartelera")
    print("2. Reservar boletos")
    print("3. Ver mis reservas")
    print("4. Salir")


# Crear el cine y agregar funciones iniciales
cine = Cine()
cine.agregar_funcion(Pelicula("Spider-Man: Multiverso", 120, "Todo público"))
cine.agregar_funcion(Pelicula("El Conjuro 4", 100, "Mayores de 16"))
cine.agregar_funcion(Pelicula("Inside Out 2", 95, "Todo público"))

# Crear cliente con su nombre ingresado por consola
nombre_cliente = input("Por favor, ingresa tu nombre: ")
cliente = Cliente(nombre_cliente)

# Bucle principal del menú interactivo
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        cine.mostrar_cartelera()

    elif opcion == "2":
        cine.mostrar_cartelera()
        try:
            seleccion = int(input("Selecciona el número de la película: ")) - 1
            cantidad = int(input("¿Cuántos boletos deseas reservar?: "))
            if 0 <= seleccion < len(cine.funciones):
                cliente.reservar(cine.funciones[seleccion], cantidad)
            else:
                print("❌ Selección no válida.\n")
        except ValueError:
            print("❌ Entrada inválida.\n")

    elif opcion == "3":
        cliente.mostrar_reservas()

    elif opcion == "4":
        print("👋 ¡Gracias por visitar el Cine Interactivo!")
        break

    else:
        print("❌ Opción inválida. Intenta de nuevo.\n")
        # Corrección del mensaje de commit anterior
