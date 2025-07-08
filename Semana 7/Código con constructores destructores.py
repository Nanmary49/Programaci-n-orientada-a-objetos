class Usuario:
    """
    Clase que representa un usuario que abre un archivo de texto.
    Usa el constructor para inicializar datos y abrir el archivo.
    Usa el destructor para cerrar el archivo automáticamente.
    """

    def __init__(self, nombre, archivo):
        """
        Constructor: se ejecuta automáticamente al crear el objeto.
        Inicializa el nombre del usuario y abre el archivo indicado.
        """
        self.nombre = nombre
        self.archivo = archivo
        try:
            self.f = open(archivo, 'w')
            print(f"[INFO] Archivo '{archivo}' abierto por {self.nombre}.")
        except Exception as e:
            print(f"[ERROR] No se pudo abrir el archivo: {e}")
            self.f = None

    def escribir_mensaje(self, mensaje):
        """
        Escribe un mensaje en el archivo si está abierto.
        """
        if self.f:
            self.f.write(mensaje + '\n')
            print(f"[INFO] Mensaje escrito por {self.nombre}.")
        else:
            print("[ADVERTENCIA] No se puede escribir. Archivo no abierto.")

    def __del__(self):
        """
        Destructor: se ejecuta automáticamente cuando el objeto es destruido.
        Cierra el archivo abierto por seguridad.
        """
        if self.f:
            self.f.close()
            print(f"[INFO] Archivo '{self.archivo}' cerrado por {self.nombre}.")


# --------------------------
# Uso del programa principal
# --------------------------
if __name__ == "__main__":
    usuario1 = Usuario("Nancy", "saludo.txt")
    usuario1.escribir_mensaje("Hola, este es un mensaje de bienvenida.")

    # El destructor se ejecuta automáticamente cuando el objeto deja de usarse
    # o al finalizar el programa. También se puede forzar con `del usuario1`.

    # Forzar eliminación del objeto (opcional, solo para demostrar __del__)
    del usuario1

    print("[INFO] Fin del programa.")
