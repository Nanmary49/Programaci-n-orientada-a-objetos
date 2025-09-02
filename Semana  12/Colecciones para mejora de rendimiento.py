"""
Sistema de Gestión para Biblioteca Digital "El Saber es Poder"
Desarrollado por: Nancy
Fecha: [Fecha actual]
Descripción: Este sistema permite administrar libros, usuarios y préstamos
             de la biblioteca digital siguiendo los requisitos especificados.
"""


class Libro:
    """
    Clase que representa un libro en la biblioteca digital.
    Utiliza tuplas para almacenar atributos inmutables como autor y título.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para autor y título (inmutables)
        self.datos_principales = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn  # ISBN como identificador único
        self.disponible = True  # Estado de disponibilidad del libro

    def __str__(self):
        return f"'{self.datos_principales[0]}' por {self.datos_principales[1]} - {self.categoria} (ISBN: {self.isbn})"


class Usuario:
    """
    Clase que representa a un usuario de la biblioteca.
    Gestiona los libros prestados al usuario mediante una lista.
    """

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario  # ID único del usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def tomar_libro(self, libro):
        """Añade un libro a la lista de libros prestados del usuario."""
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        """Remueve un libro de la lista de libros prestados del usuario."""
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    """
    Clase principal que gestiona la biblioteca digital "El Saber es Poder".
    Utiliza diversas estructuras de datos para una gestión eficiente.
    """

    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la biblioteca
        self.libros = {}  # Diccionario para libros (clave: ISBN, valor: objeto Libro)
        self.usuarios = {}  # Diccionario para usuarios (clave: ID usuario, valor: objeto Usuario)
        self.ids_usuarios = set()  # Conjunto para IDs de usuarios únicos
        self.historial_prestamos = []  # Lista para registrar el historial de préstamos

    def añadir_libro(self, libro):
        """Añade un nuevo libro al catálogo de la biblioteca."""
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
            return False
        self.libros[libro.isbn] = libro
        print(f"Libro '{libro.datos_principales[0]}' añadido exitosamente.")
        return True

    def quitar_libro(self, isbn):
        """Elimina un libro del catálogo de la biblioteca."""
        if isbn in self.libros:
            libro = self.libros[isbn]
            if not libro.disponible:
                print(f"No se puede eliminar el libro '{libro.datos_principales[0]}' porque está prestado.")
                return False
            del self.libros[isbn]
            print(f"Libro '{libro.datos_principales[0]}' eliminado exitosamente.")
            return True
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}.")
            return False

    def registrar_usuario(self, nombre, id_usuario):
        """Registra un nuevo usuario en el sistema de la biblioteca."""
        if id_usuario in self.ids_usuarios:
            print(f"El ID de usuario {id_usuario} ya está registrado.")
            return False

        nuevo_usuario = Usuario(nombre, id_usuario)
        self.usuarios[id_usuario] = nuevo_usuario
        self.ids_usuarios.add(id_usuario)
        print(f"Usuario '{nombre}' registrado exitosamente con ID {id_usuario}.")
        return True

    def dar_baja_usuario(self, id_usuario):
        """Da de baja a un usuario del sistema de la biblioteca."""
        if id_usuario not in self.usuarios:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")
            return False

        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"No se puede dar de baja al usuario {usuario.nombre} porque tiene libros prestados.")
            return False

        del self.usuarios[id_usuario]
        self.ids_usuarios.remove(id_usuario)
        print(f"Usuario '{usuario.nombre}' dado de baja exitosamente.")
        return True

    def prestar_libro(self, isbn, id_usuario):
        """Gestiona el préstamo de un libro a un usuario."""
        if isbn not in self.libros:
            print(f"No se encontró ningún libro con ISBN {isbn}.")
            return False

        if id_usuario not in self.usuarios:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")
            return False

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if not libro.disponible:
            print(f"El libro '{libro.datos_principales[0]}' no está disponible para préstamo.")
            return False

        # Realizar el préstamo
        libro.disponible = False
        usuario.tomar_libro(libro)

        # Registrar en el historial
        self.historial_prestamos.append({
            'accion': 'préstamo',
            'libro': libro.datos_principales[0],
            'isbn': isbn,
            'usuario': usuario.nombre,
            'id_usuario': id_usuario,
            'fecha': '2024-05-15'  # En una implementación real, usaría datetime.now()
        })

        print(f"Libro '{libro.datos_principales[0]}' prestado a {usuario.nombre} exitosamente.")
        return True

    def devolver_libro(self, isbn, id_usuario):
        """Gestiona la devolución de un libro por parte de un usuario."""
        if isbn not in self.libros:
            print(f"No se encontró ningún libro con ISBN {isbn}.")
            return False

        if id_usuario not in self.usuarios:
            print(f"No se encontró ningún usuario with ID {id_usuario}.")
            return False

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if libro not in usuario.libros_prestados:
            print(f"El usuario {usuario.nombre} no tiene prestado el libro '{libro.datos_principales[0]}'.")
            return False

        # Procesar la devolución
        libro.disponible = True
        usuario.devolver_libro(libro)

        # Registrar en el historial
        self.historial_prestamos.append({
            'accion': 'devolución',
            'libro': libro.datos_principales[0],
            'isbn': isbn,
            'usuario': usuario.nombre,
            'id_usuario': id_usuario,
            'fecha': '2024-05-15'  # En una implementación real, usaría datetime.now()
        })

        print(f"Libro '{libro.datos_principales[0]}' devuelto por {usuario.nombre} exitosamente.")
        return True

    def buscar_libros(self, criterio, valor):
        """Busca libros por título, autor o categoría."""
        resultados = []

        for isbn, libro in self.libros.items():
            if criterio == 'titulo' and valor.lower() in libro.datos_principales[0].lower():
                resultados.append(libro)
            elif criterio == 'autor' and valor.lower() in libro.datos_principales[1].lower():
                resultados.append(libro)
            elif criterio == 'categoria' and valor.lower() in libro.categoria.lower():
                resultados.append(libro)

        return resultados

    def listar_libros_prestados(self, id_usuario):
        """Lista todos los libros prestados a un usuario específico."""
        if id_usuario not in self.usuarios:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")
            return None

        usuario = self.usuarios[id_usuario]
        return usuario.libros_prestados

    def __str__(self):
        return (f"Biblioteca: {self.nombre}\n"
                f"Total de libros: {len(self.libros)}\n"
                f"Total de usuarios: {len(self.usuarios)}\n"
                f"Préstamos en curso: {sum(1 for libro in self.libros.values() if not libro.disponible)}")


# Creación de la biblioteca "El Saber es Poder"
biblioteca = Biblioteca("El Saber es Poder")

# Añadiendo libros al catálogo
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "978-8437604947")
libro2 = Libro("1984", "George Orwell", "Ciencia ficción", "978-0451524935")
libro3 = Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", "978-0156012195")
libro4 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", "978-8424112936")

biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)
biblioteca.añadir_libro(libro4)

# Registrando usuarios
biblioteca.registrar_usuario("Ana García", "U001")
biblioteca.registrar_usuario("Carlos Rodríguez", "U002")
biblioteca.registrar_usuario("María López", "U003")

# Realizando préstamos de libros
biblioteca.prestar_libro("978-8437604947", "U001")  # Cien años de soledad a Ana
biblioteca.prestar_libro("978-0451524935", "U002")  # 1984 a Carlos
biblioteca.prestar_libro("978-0156012195", "U001")  # El principito a Ana

# Intentando prestar un libro ya prestado
biblioteca.prestar_libro("978-0156012195", "U003")  # Intentando prestar El principito a María

# Buscando libros por autor
print("\nBuscando libros de Gabriel García Márquez:")
resultados = biblioteca.buscar_libros('autor', 'Gabriel García Márquez')
for libro in resultados:
    print(f" - {libro}")

# Listando libros prestados a un usuario
print(f"\nLibros prestados a Ana García:")
libros_ana = biblioteca.listar_libros_prestados("U001")
for libro in libros_ana:
    print(f" - {libro.datos_principales[0]}")

# Devolviendo un libro
biblioteca.devolver_libro("978-0156012195", "U001")  # Ana devuelve El principito

# Intentando dar de baja a un usuario con libros prestados
biblioteca.dar_baja_usuario("U002")  # Carlos todavía tiene un libro prestado

# Mostrando el estado actual de la biblioteca
print(f"\nEstado actual de la biblioteca:")
print(biblioteca)