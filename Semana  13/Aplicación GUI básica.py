import tkinter as tk
from tkinter import messagebox, ttk


class AplicacionTareas:
    """Clase principal que define la aplicación de gestión de tareas personales"""

    def __init__(self, ventana_principal):
        """
        Inicializa la aplicación con todos sus componentes

        Args:
            ventana_principal: La ventana raíz de Tkinter donde se construirán los componentes
        """
        # Configuración de la ventana principal
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Gestor de Tareas Personales - Aplicación GUI")
        self.ventana_principal.geometry("700x500")  # Tamaño inicial de la ventana
        self.ventana_principal.resizable(True, True)  # Permite redimensionar la ventana

        # Inicializar la lista de tareas (estructura de datos)
        self.lista_tareas = []

        # Configurar el estilo de los componentes
        self.configurar_estilos()

        # Construir la interfaz de usuario
        self.construir_interfaz()

    def configurar_estilos(self):
        """Configura los estilos visuales para los componentes de la interfaz"""
        self.estilo = ttk.Style()
        self.estilo.configure('Titulo.TLabel', font=('Arial', 16, 'bold'), foreground='#2E86AB')
        self.estilo.configure('Normal.TLabel', font=('Arial', 10))
        self.estilo.configure('Boton.TButton', font=('Arial', 10), background='#2E86AB')
        self.estilo.configure('Campo.TEntry', font=('Arial', 10))

    def construir_interfaz(self):
        """Construye todos los componentes de la interfaz gráfica"""
        # Marco principal para organizar los componentes
        marco_principal = ttk.Frame(self.ventana_principal, padding="10")
        marco_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar la expansión de las filas y columnas
        self.ventana_principal.columnconfigure(0, weight=1)
        self.ventana_principal.rowconfigure(0, weight=1)
        marco_principal.columnconfigure(1, weight=1)
        marco_principal.rowconfigure(5, weight=1)

        # Título de la aplicación
        titulo = ttk.Label(marco_principal, text="Gestor de Tareas Personales", style='Titulo.TLabel')
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Etiqueta y campo de texto para el nombre de la tarea
        etiqueta_nombre = ttk.Label(marco_principal, text="Nombre de Tarea:", style='Normal.TLabel')
        etiqueta_nombre.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))

        self.campo_nombre = ttk.Entry(marco_principal, width=40, style='Campo.TEntry')
        self.campo_nombre.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=(0, 5))

        # Etiqueta y campo de texto para la descripción de la tarea
        etiqueta_descripcion = ttk.Label(marco_principal, text="Descripción:", style='Normal.TLabel')
        etiqueta_descripcion.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))

        self.campo_descripcion = ttk.Entry(marco_principal, width=40, style='Campo.TEntry')
        self.campo_descripcion.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=(0, 5))
        self.campo_descripcion.bind('<Return>', lambda event: self.agregar_tarea())  # Permitir agregar con Enter

        # Marco para los botones
        marco_botones = ttk.Frame(marco_principal)
        marco_botones.grid(row=3, column=0, columnspan=2, pady=(10, 10))

        # Botón para agregar tarea
        boton_agregar = ttk.Button(marco_botones, text="Agregar Tarea",
                                   command=self.agregar_tarea, style='Boton.TButton')
        boton_agregar.grid(row=0, column=0, padx=(0, 10))

        # Botón para limpiar campos
        boton_limpiar_campos = ttk.Button(marco_botones, text="Limpiar Campos",
                                          command=self.limpiar_campos, style='Boton.TButton')
        boton_limpiar_campos.grid(row=0, column=1, padx=(0, 10))

        # Botón para limpiar selección
        boton_limpiar_seleccion = ttk.Button(marco_botones, text="Limpiar Selección",
                                             command=self.limpiar_seleccion, style='Boton.TButton')
        boton_limpiar_seleccion.grid(row=0, column=2, padx=(0, 10))

        # Botón para eliminar tarea seleccionada
        boton_eliminar = ttk.Button(marco_botones, text="Eliminar Tarea",
                                    command=self.eliminar_tarea, style='Boton.TButton')
        boton_eliminar.grid(row=0, column=3)

        # Etiqueta para la lista de tareas
        etiqueta_lista = ttk.Label(marco_principal, text="Tareas Pendientes:", style='Normal.TLabel')
        etiqueta_lista.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))

        # Lista de tareas con scrollbar
        # Marco para contener la lista y la barra de desplazamiento
        marco_lista = ttk.Frame(marco_principal)
        marco_lista.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        marco_lista.columnconfigure(0, weight=1)
        marco_lista.rowconfigure(0, weight=1)

        # Crear un Treeview (tabla) para mostrar las tareas con nombre y descripción
        columnas = ('nombre', 'descripcion')
        self.lista_tareas_widget = ttk.Treeview(marco_lista, columns=columnas, show='headings', height=12)

        # Configurar las columnas
        self.lista_tareas_widget.heading('nombre', text='Nombre de Tarea')
        self.lista_tareas_widget.column('nombre', width=200, anchor=tk.W)

        self.lista_tareas_widget.heading('descripcion', text='Descripción')
        self.lista_tareas_widget.column('descripcion', width=350, anchor=tk.W)

        # Barra de desplazamiento vertical
        scrollbar = ttk.Scrollbar(marco_lista, orient=tk.VERTICAL, command=self.lista_tareas_widget.yview)
        self.lista_tareas_widget.configure(yscrollcommand=scrollbar.set)

        # Colocar los componentes en el marco de la lista
        self.lista_tareas_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Etiqueta para el pie de página
        pie_pagina = ttk.Label(marco_principal, text="© 2023 - Aplicación GUI de Gestión de Tareas Personales",
                               style='Normal.TLabel')
        pie_pagina.grid(row=6, column=0, columnspan=2, pady=(20, 0))

    def agregar_tarea(self):
        """
        Agrega una nueva tarea a la lista a partir del nombre y descripción ingresados.
        Valida que los campos no estén vacíos antes de agregar.
        """
        # Obtener el texto de los campos de entrada
        nombre_tarea = self.campo_nombre.get().strip()
        descripcion_tarea = self.campo_descripcion.get().strip()

        # Validar que los campos no estén vacíos
        if not nombre_tarea:
            messagebox.showwarning("Campo Vacío", "Por favor, ingresa un nombre para la tarea antes de agregar.")
            self.campo_nombre.focus()
            return

        if not descripcion_tarea:
            messagebox.showwarning("Campo Vacío", "Por favor, ingresa una descripción para la tarea antes de agregar.")
            self.campo_descripcion.focus()
            return

        # Crear un diccionario con la información de la tarea
        tarea = {
            'nombre': nombre_tarea,
            'descripcion': descripcion_tarea
        }

        # Agregar la tarea a la lista interna
        self.lista_tareas.append(tarea)

        # Agregar la tarea al widget de lista (Treeview)
        self.lista_tareas_widget.insert('', tk.END, values=(nombre_tarea, descripcion_tarea))

        # Limpiar los campos de entrada después de agregar
        self.limpiar_campos()

        # Enfocar nuevamente el campo de nombre para facilitar la entrada de más tareas
        self.campo_nombre.focus()

    def limpiar_campos(self):
        """Limpia los campos de entrada de nombre y descripción"""
        self.campo_nombre.delete(0, tk.END)
        self.campo_descripcion.delete(0, tk.END)

    def limpiar_seleccion(self):
        """Limpia la selección actual en la lista de tareas"""
        # Deseleccionar cualquier elemento seleccionado en la lista
        seleccion = self.lista_tareas_widget.selection()
        if seleccion:
            self.lista_tareas_widget.selection_remove(seleccion)

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada de la lista"""
        # Obtener la selección actual
        seleccion = self.lista_tareas_widget.selection()

        # Verificar que haya una selección
        if not seleccion:
            messagebox.showwarning("Nada Seleccionado", "Por favor, selecciona una tarea para eliminar.")
            return

        # Obtener los valores del elemento seleccionado
        valores = self.lista_tareas_widget.item(seleccion[0], 'values')
        nombre_tarea = valores[0] if valores else "esta tarea"

        # Confirmar la eliminación
        confirmar = messagebox.askyesno("Confirmar Eliminación",
                                        f"¿Estás seguro de que quieres eliminar la tarea '{nombre_tarea}'?")

        if confirmar:
            # Eliminar de la lista interna
            for item in seleccion:
                # Obtener los valores del elemento seleccionado
                valores = self.lista_tareas_widget.item(item, 'values')

                # Buscar y eliminar la tarea correspondiente en la lista interna
                for tarea in self.lista_tareas:
                    if tarea['nombre'] == valores[0] and tarea['descripcion'] == valores[1]:
                        self.lista_tareas.remove(tarea)
                        break

                # Eliminar del widget de lista
                self.lista_tareas_widget.delete(item)


def main():
    """
    Función principal que inicia la aplicación.
    Crea la ventana principal y la instancia de la aplicación.
    """
    # Crear la ventana principal de Tkinter
    ventana_principal = tk.Tk()

    # Crear la instancia de la aplicación
    aplicacion = AplicacionTareas(ventana_principal)

    # Iniciar el bucle principal de eventos
    ventana_principal.mainloop()


# Punto de entrada del programa
if __name__ == "__main__":
    main()