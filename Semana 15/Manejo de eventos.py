import tkinter as tk
from tkinter import ttk, messagebox


class AplicacionListaTareas:
    def __init__(self, root):
        """
        Constructor de la aplicación - aquí inicializamos todos los componentes
        """
        self.root = root
        self.root.title("Lista de Tareas - Desarrollado por Nancy Campos")
        self.root.geometry("500x400")
        self.root.resizable(True, True)

        # Lista para almacenar nuestras tareas y sus estados
        # Cada tarea será un diccionario: {'texto': 'Tarea 1', 'completada': False}
        self.tareas = []

        # Configurar el estilo visual de la aplicación
        self.configurar_estilos()

        # Construir la interfaz gráfica
        self.construir_interfaz()

        # Cargar algunas tareas de ejemplo (opcional)
        self.cargar_tareas_ejemplo()

    def configurar_estilos(self):
        """Configura los estilos visuales para que la app se vea más moderna"""
        style = ttk.Style()
        style.configure('Titulo.TLabel', font=('Arial', 16, 'bold'), foreground='#2c3e50')
        style.configure('BotonAgregar.TButton', font=('Arial', 10), background='#27ae60')
        style.configure('BotonCompletar.TButton', font=('Arial', 10), background='#3498db')
        style.configure('BotonEliminar.TButton', font=('Arial', 10), background='#e74c3c')

    def construir_interfaz(self):
        """Construye todos los elementos de la interfaz gráfica"""

        # Título principal de la aplicación
        titulo = ttk.Label(self.root, text="📝 Mi Lista de Tareas - por Nancy Campos", style='Titulo.TLabel')
        titulo.pack(pady=10)

        # Marco para el área de entrada de nuevas tareas
        marco_entrada = ttk.Frame(self.root)
        marco_entrada.pack(pady=10, padx=20, fill='x')

        # Etiqueta para el campo de entrada
        lbl_nueva_tarea = ttk.Label(marco_entrada, text="Nueva tarea:")
        lbl_nueva_tarea.pack(side='left')

        # Campo de entrada de texto para nuevas tareas
        self.entrada_tarea = ttk.Entry(marco_entrada, width=40)
        self.entrada_tarea.pack(side='left', padx=5, fill='x', expand=True)

        # Enfocar el campo de entrada automáticamente al iniciar la app
        self.entrada_tarea.focus()

        # Botón para añadir tareas
        btn_agregar = ttk.Button(marco_entrada, text="➕ Agregar",
                                 command=self.agregar_tarea, style='BotonAgregar.TButton')
        btn_agregar.pack(side='left', padx=5)

        # Marco para la lista de tareas
        marco_lista = ttk.Frame(self.root)
        marco_lista.pack(pady=10, padx=20, fill='both', expand=True)

        # Crear un Treeview para mostrar las tareas de forma más organizada
        self.lista_tareas = ttk.Treeview(marco_lista, columns=('estado'), show='tree headings', height=12)
        self.lista_tareas.heading('#0', text='Tarea')
        self.lista_tareas.heading('estado', text='Estado')
        self.lista_tareas.column('#0', width=350)
        self.lista_tareas.column('estado', width=100)

        # Scrollbar para la lista de tareas
        scrollbar = ttk.Scrollbar(marco_lista, orient='vertical', command=self.lista_tareas.yview)
        self.lista_tareas.configure(yscrollcommand=scrollbar.set)

        self.lista_tareas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Marco para los botones de acción
        marco_botones = ttk.Frame(self.root)
        marco_botones.pack(pady=10)

        # Botón para marcar tarea como completada
        btn_completar = ttk.Button(marco_botones, text="✅ Completar",
                                   command=self.marcar_completada, style='BotonCompletar.TButton')
        btn_completar.pack(side='left', padx=5)

        # Botón para eliminar tarea
        btn_eliminar = ttk.Button(marco_botones, text="🗑️ Eliminar",
                                  command=self.eliminar_tarea, style='BotonEliminar.TButton')
        btn_eliminar.pack(side='left', padx=5)

        # Botón para limpiar todas las tareas completadas
        btn_limpiar = ttk.Button(marco_botones, text="🧹 Limpiar Completadas",
                                 command=self.limpiar_completadas)
        btn_limpiar.pack(side='left', padx=5)

        # Pie de página con el nombre de la desarrolladora
        pie_pagina = ttk.Label(self.root, text="Desarrollado con ❤️ por Nancy Campos",
                               font=('Arial', 9, 'italic'), foreground='#7f8c8d')
        pie_pagina.pack(side='bottom', pady=8)

        # Configurar eventos del teclado
        self.configurar_eventos_teclado()

    def configurar_eventos_teclado(self):
        """
        Configura los eventos de teclado para mejorar la experiencia de usuario
        """
        # Enter en el campo de entrada agrega nueva tarea
        self.entrada_tarea.bind('<Return>', lambda event: self.agregar_tarea())

        # Delete key elimina la tarea seleccionada
        self.root.bind('<Delete>', lambda event: self.eliminar_tarea())

        # Space key marca como completada la tarea seleccionada
        self.root.bind('<space>', lambda event: self.marcar_completada())

        # Doble clic en una tarea la marca como completada
        self.lista_tareas.bind('<Double-1>', lambda event: self.marcar_completada())

    def cargar_tareas_ejemplo(self):
        """Carga algunas tareas de ejemplo para mostrar cómo funciona la app"""
        tareas_ejemplo = [
            "Aprender Tkinter con Nancy Campos",
            "Completar la aplicación de tareas",
            "Probar todas las funcionalidades",
            "Personalizar la interfaz a mi gusto"
        ]

        for tarea in tareas_ejemplo:
            self.tareas.append({'texto': tarea, 'completada': False})

        self.actualizar_lista()

    def agregar_tarea(self):
        """
        Agrega una nueva tarea a la lista desde el campo de entrada
        """
        texto_tarea = self.entrada_tarea.get().strip()

        # Validar que la tarea no esté vacía
        if not texto_tarea:
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea antes de agregarla.")
            return

        # Validar que la tarea no exista ya
        if any(tarea['texto'].lower() == texto_tarea.lower() for tarea in self.tareas):
            messagebox.showwarning("Advertencia", "Esta tarea ya existe en la lista.")
            return

        # Agregar la nueva tarea a nuestra lista
        nueva_tarea = {
            'texto': texto_tarea,
            'completada': False
        }
        self.tareas.append(nueva_tarea)

        # Limpiar el campo de entrada y actualizar la lista visual
        self.entrada_tarea.delete(0, tk.END)
        self.actualizar_lista()

        # Mensaje de confirmación (opcional)
        print(f"Tarea agregada por Nancy: {texto_tarea}")

    def marcar_completada(self):
        """
        Marca la tarea seleccionada como completada o pendiente
        """
        seleccion = self.lista_tareas.selection()

        if not seleccion:
            messagebox.showinfo("Información", "Por favor, selecciona una tarea primero.")
            return

        # Obtener el índice de la tarea seleccionada
        item_seleccionado = seleccion[0]
        indice = self.lista_tareas.index(item_seleccionado)

        # Cambiar el estado de la tarea (completada ↔ pendiente)
        self.tareas[indice]['completada'] = not self.tareas[indice]['completada']

        # Actualizar la lista visual
        self.actualizar_lista()

        # Mostrar mensaje de estado
        estado = "completada" if self.tareas[indice]['completada'] else "pendiente"
        print(f"Tarea marcada como {estado} por Nancy: {self.tareas[indice]['texto']}")

    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada de la lista
        """
        seleccion = self.lista_tareas.selection()

        if not seleccion:
            messagebox.showinfo("Información", "Por favor, selecciona una tarea para eliminar.")
            return

        # Confirmar eliminación
        item_seleccionado = seleccion[0]
        valores = self.lista_tareas.item(item_seleccionado, 'values')
        texto_tarea = self.lista_tareas.item(item_seleccionado)['text']

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Estás seguro de que quieres eliminar la tarea: '{texto_tarea}'?"
        )

        if confirmar:
            # Obtener índice y eliminar
            indice = self.lista_tareas.index(item_seleccionado)
            tarea_eliminada = self.tareas.pop(indice)

            # Actualizar la lista visual
            self.actualizar_lista()

            print(f"Tarea eliminada por Nancy: {tarea_eliminada['texto']}")

    def limpiar_completadas(self):
        """
        Elimina todas las tareas marcadas como completadas
        """
        # Contar tareas completadas
        tareas_completadas = [t for t in self.tareas if t['completada']]

        if not tareas_completadas:
            messagebox.showinfo("Información", "No hay tareas completadas para limpiar.")
            return

        # Confirmar limpieza
        confirmar = messagebox.askyesno(
            "Confirmar limpieza",
            f"¿Estás seguro de que quieres eliminar {len(tareas_completadas)} tareas completadas?"
        )

        if confirmar:
            # Mantener solo las tareas pendientes
            self.tareas = [t for t in self.tareas if not t['completada']]

            # Actualizar la lista visual
            self.actualizar_lista()

            print(f"Nancy eliminó {len(tareas_completadas)} tareas completadas")

    def mostrar_creditos(self):
        """Muestra los créditos de la aplicación"""
        messagebox.showinfo("Créditos - Nancy Campos",
                            "🎉 Lista de Tareas Personalizada\n\n"
                            "Desarrollado por: Nancy Campos\n"
                            "Versión: 1.0\n"
                            "Fecha: 2024\n\n"
                            "¡Gracias por usar mi aplicación!")

    def actualizar_lista(self):
        """
        Actualiza la lista visual de tareas reflejando los cambios actuales
        """
        # Limpiar la lista actual
        for item in self.lista_tareas.get_children():
            self.lista_tareas.delete(item)

        # Agregar cada tarea con su estado actual
        for tarea in self.tareas:
            texto = tarea['texto']
            estado = "✅ Completada" if tarea['completada'] else "⏳ Pendiente"

            # Aplicar formato diferente según el estado
            if tarea['completada']:
                # Tachado para tareas completadas
                item = self.lista_tareas.insert('', 'end', text=texto, values=(estado))
                self.lista_tareas.item(item, tags=('completada',))
            else:
                self.lista_tareas.insert('', 'end', text=texto, values=(estado))

        # Configurar el estilo para tareas completadas
        self.lista_tareas.tag_configure('completada', foreground='gray')

    def ejecutar(self):
        """Método para iniciar la aplicación"""
        self.root.mainloop()


# Función principal para ejecutar la aplicación
def main():
    """
    Función principal que inicia nuestra aplicación de lista de tareas
    """
    try:
        # Crear la ventana principal
        root = tk.Tk()

        # Crear nuestra aplicación
        app = AplicacionListaTareas(root)

        # Mostrar mensaje de inicio en consola
        print("🚀 Aplicación de Lista de Tareas - por Nancy Campos")
        print("📋 Comandos disponibles:")
        print("   - Enter: Agregar tarea")
        print("   - Espacio: Marcar como completada")
        print("   - Delete: Eliminar tarea")
        print("   - Doble clic: Marcar como completada")
        print("   - Botón derecho: Ver créditos de Nancy")

        # Agregar evento de clic derecho para mostrar créditos
        app.root.bind('<Button-3>', lambda event: app.mostrar_creditos())

        # Iniciar el bucle principal de la aplicación
        app.ejecutar()

    except Exception as e:
        print(f"❌ Error al iniciar la aplicación: {e}")
        messagebox.showerror("Error", f"No se pudo iniciar la aplicación:\n{e}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()