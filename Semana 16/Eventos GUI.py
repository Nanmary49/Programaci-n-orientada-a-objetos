import tkinter as tk
from tkinter import ttk, messagebox


class TaskManagerApp:
    def __init__(self, root):
        # Inicializamos la ventana principal con tu nombre en el título
        self.root = root
        self.root.title("🎯 Gestor de Tareas - Nancy Campos")  # ¡Aquí va tu nombre!
        self.root.geometry("600x400")
        self.root.configure(bg='#f0f0f0')

        # Aquí guardaremos todas nuestras tareas como una lista de diccionarios
        # Cada tarea tendrá su texto y si está completada o no
        self.tasks = []

        # Construimos todos los elementos de la interfaz
        self.create_widgets()

        # Configuramos los atajos de teclado para ser más productivos
        self.setup_keyboard_shortcuts()

    def create_widgets(self):
        """Construimos pieza por pieza la interfaz que el usuario verá"""
        # Frame principal que contendrá todos los elementos
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configuramos cómo se expanden los elementos cuando cambia el tamaño de la ventana
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Título principal de la aplicación con tu nombre
        title_label = ttk.Label(main_frame, text="🎯 Gestor de Tareas - Nancy Campos",
                                font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15))

        # Área donde escribiremos nuevas tareas
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(0, weight=1)

        # Etiqueta que indica dónde escribir
        ttk.Label(input_frame, text="📝 ¿Qué necesitas hacer?").grid(row=0, column=0, sticky=tk.W)

        # Campo de texto donde escribimos nuestras nuevas tareas
        self.task_entry = ttk.Entry(input_frame, font=('Arial', 11))
        self.task_entry.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(5, 5))
        self.task_entry.focus()  # Hacemos que el cursor esté listo para escribir inmediatamente

        # Panel con todos los botones de acción
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=2, column=0, columnspan=3, pady=(0, 15))

        # Botón para añadir nuevas tareas - AHORA CON COLORES VISIBLES
        self.add_button = tk.Button(buttons_frame,
                                    text="➕ Añadir Tarea (Enter)",
                                    command=self.add_task,
                                    bg='#4CAF50',  # Fondo verde
                                    fg='white',  # Texto blanco
                                    font=('Arial', 10, 'bold'),
                                    padx=15,
                                    pady=8,
                                    relief='raised',
                                    bd=2)
        self.add_button.grid(row=0, column=0, padx=(0, 10))

        # Botón para marcar tareas como completadas
        self.complete_button = tk.Button(buttons_frame,
                                         text="✅ Completar (C)",
                                         command=self.complete_task,
                                         bg='#2196F3',  # Fondo azul
                                         fg='white',  # Texto blanco
                                         font=('Arial', 10, 'bold'),
                                         padx=15,
                                         pady=8,
                                         relief='raised',
                                         bd=2)
        self.complete_button.grid(row=0, column=1, padx=(0, 10))

        # Botón para eliminar tareas
        self.delete_button = tk.Button(buttons_frame,
                                       text="🗑️ Eliminar (Delete)",
                                       command=self.delete_task,
                                       bg='#f44336',  # Fondo rojo
                                       fg='white',  # Texto blanco
                                       font=('Arial', 10, 'bold'),
                                       padx=15,
                                       pady=8,
                                       relief='raised',
                                       bd=2)
        self.delete_button.grid(row=0, column=2)

        # Área donde se muestra la lista de tareas
        list_frame = ttk.LabelFrame(main_frame, text="📋 Tu Lista de Tareas", padding="5")
        list_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Creamos la lista visual de tareas
        self.create_task_list(list_frame)

        # Pequeña ayuda que muestra los atajos de teclado disponibles
        shortcuts_label = ttk.Label(main_frame,
                                    text="⌨️ Atajos: Enter=Añadir | C=Completar | Delete=Eliminar | Escape=Salir",
                                    font=('Arial', 9), foreground='gray')
        shortcuts_label.grid(row=4, column=0, columnspan=3, pady=(10, 0))

    def create_task_list(self, parent):
        """Creamos la lista desplazable donde veremos todas nuestras tareas"""
        # Contenedor para la lista y la barra de desplazamiento
        list_container = ttk.Frame(parent)
        list_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        list_container.columnconfigure(0, weight=1)
        list_container.rowconfigure(0, weight=1)

        # Barra de desplazamiento para cuando tengamos muchas tareas
        scrollbar = ttk.Scrollbar(list_container)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # La lista principal donde se muestran las tareas
        self.task_listbox = tk.Listbox(list_container,
                                       yscrollcommand=scrollbar.set,
                                       font=('Arial', 11),
                                       selectbackground='#e0e0e0',
                                       selectmode=tk.SINGLE,  # Solo se puede seleccionar una tarea a la vez
                                       height=12)
        self.task_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Conectamos la barra de desplazamiento con la lista
        scrollbar.config(command=self.task_listbox.yview)

    def setup_keyboard_shortcuts(self):
        """Configuramos los atajos de teclado para trabajar más rápido"""
        # Enter: Añadir nueva tarea rápidamente
        self.root.bind('<Return>', lambda event: self.add_task())

        # Tecla C: Marcar tarea como completada (minúscula y mayúscula)
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<C>', lambda event: self.complete_task())

        # Tecla Delete o D: Eliminar tarea seleccionada
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<D>', lambda event: self.delete_task())

        # Escape: Salir rápidamente de la aplicación
        self.root.bind('<Escape>', lambda event: self.root.quit())

        # Si hacemos clic en cualquier lugar vacío, el cursor vuelve al campo de texto
        self.root.bind('<Button-1>', self.focus_entry)

    def focus_entry(self, event):
        """Cuando hacemos clic en la ventana principal, el cursor vuelve al campo de texto"""
        if event.widget == self.root:
            self.task_entry.focus()

    def add_task(self):
        """Añadimos una nueva tarea a nuestra lista"""
        # Obtenemos el texto que escribió el usuario y quitamos espacios extra
        task_text = self.task_entry.get().strip()

        # Verificamos que no esté vacío
        if task_text:
            # Guardamos la nueva tarea en nuestra lista
            self.tasks.append({
                'text': task_text,
                'completed': False  # Al inicio siempre está pendiente
            })

            # Actualizamos la lista visual para que muestre la nueva tarea
            self.update_task_list()

            # Limpiamos el campo de texto para escribir la siguiente tarea
            self.task_entry.delete(0, tk.END)

            # Ponemos el cursor listo para escribir otra tarea
            self.task_entry.focus()
        else:
            # Si el usuario intenta añadir una tarea vacía, le mostramos un mensaje amigable
            messagebox.showwarning("¡Ups!", "Por favor, escribe una tarea antes de añadirla.")

    def complete_task(self):
        """Marcamos una tarea como completada (o la volvemos a poner como pendiente)"""
        # Verificamos qué tarea tiene el usuario seleccionada
        selected_index = self.task_listbox.curselection()

        if selected_index:
            index = selected_index[0]
            if 0 <= index < len(self.tasks):
                # Cambiamos el estado de la tarea (si estaba completada, la descompletamos y viceversa)
                self.tasks[index]['completed'] = not self.tasks[index]['completed']

                # Actualizamos la lista visual para mostrar el cambio
                self.update_task_list()

                # Mantenemos la misma tarea seleccionada después del cambio
                if index < len(self.tasks):
                    self.task_listbox.selection_set(index)
        else:
            # Si no hay ninguna tarea seleccionada, le recordamos al usuario que debe seleccionar una
            messagebox.showinfo("Selecciona una tarea", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        """Eliminamos una tarea de nuestra lista"""
        # Verificamos qué tarea tiene el usuario seleccionada
        selected_index = self.task_listbox.curselection()

        if selected_index:
            index = selected_index[0]
            if 0 <= index < len(self.tasks):
                # Obtenemos el texto de la tarea para mostrarlo en la confirmación
                task_text = self.tasks[index]['text']

                # Preguntamos amablemente si realmente quiere eliminar la tarea
                if messagebox.askyesno("Confirmar eliminación",
                                       f"¿Estás seguro de que quieres eliminar esta tarea?\n\n\"{task_text}\""):
                    # Si confirma, eliminamos la tarea de nuestra lista
                    del self.tasks[index]

                    # Actualizamos la lista visual
                    self.update_task_list()
        else:
            # Si no hay ninguna tarea seleccionada, le avisamos al usuario
            messagebox.showinfo("Selecciona una tarea", "Por favor, selecciona una tarea para eliminar.")

    def update_task_list(self):
        """Actualizamos la lista visual para que muestre el estado actual de todas las tareas"""
        # Limpiamos toda la lista actual
        self.task_listbox.delete(0, tk.END)

        # Volvemos a añadir todas las tareas, pero con su formato correspondiente
        for task in self.tasks:
            task_text = task['text']
            if task['completed']:
                # Tarea completada: la mostramos con un checkmark y texto gris tachado
                self.task_listbox.insert(tk.END, f"✅ {task_text}")
                self.task_listbox.itemconfig(tk.END, {'fg': 'gray'})
            else:
                # Tarea pendiente: la mostramos con un círculo y texto negro normal
                self.task_listbox.insert(tk.END, f"⭕ {task_text}")
                self.task_listbox.itemconfig(tk.END, {'fg': 'black'})

        # Actualizamos las estadísticas en el título de la ventana
        self.update_stats()

    def update_stats(self):
        """Actualizamos el título de la ventana para mostrar nuestro progreso"""
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task['completed'])

        # Mostramos cuántas tareas hemos completado del total
        self.root.title(f"🎯 Gestor de Tareas - Nancy Campos - {completed_tasks}/{total_tasks} completadas")


def main():
    """Función principal que inicia nuestra aplicación"""
    # Creamos la ventana principal
    root = tk.Tk()

    # Creamos nuestra aplicación
    app = TaskManagerApp(root)

    # Iniciamos el bucle principal que mantiene la aplicación funcionando
    root.mainloop()


if __name__ == "__main__":
    # Si ejecutamos este archivo directamente, iniciamos la aplicación
    main()