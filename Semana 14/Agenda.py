import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os


class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal Nancy Campos")
        self.root.geometry("800x600")

        # Cargar datos existentes
        self.cargar_datos()

        # Crear interfaz
        self.crear_interfaz()

        # Cargar eventos
        self.actualizar_lista_eventos()

    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título
        titulo = ttk.Label(main_frame, text="Agenda Personal", font=("Arial", 16, "bold"))
        titulo.pack(pady=(0, 15))

        # Frame para entrada de datos
        entrada_frame = ttk.LabelFrame(main_frame, text="Nuevo Evento", padding="10")
        entrada_frame.pack(fill=tk.X, pady=(0, 10))

        # Fecha
        fecha_frame = ttk.Frame(entrada_frame)
        fecha_frame.pack(fill=tk.X, pady=5)
        ttk.Label(fecha_frame, text="Fecha (YYYY-MM-DD):").pack(side=tk.LEFT, padx=(0, 5))
        self.fecha_var = tk.StringVar()
        ttk.Entry(fecha_frame, textvariable=self.fecha_var, width=15).pack(side=tk.LEFT, padx=(0, 10))

        # Hora
        hora_frame = ttk.Frame(entrada_frame)
        hora_frame.pack(fill=tk.X, pady=5)
        ttk.Label(hora_frame, text="Hora (HH:MM):").pack(side=tk.LEFT, padx=(0, 5))
        self.hora_var = tk.StringVar(value="12:00")
        ttk.Entry(hora_frame, textvariable=self.hora_var, width=10).pack(side=tk.LEFT, padx=(0, 10))

        # Descripción
        desc_frame = ttk.Frame(entrada_frame)
        desc_frame.pack(fill=tk.X, pady=5)
        ttk.Label(desc_frame, text="Descripción:").pack(side=tk.LEFT, padx=(0, 5))
        self.descripcion_var = tk.StringVar()
        ttk.Entry(desc_frame, textvariable=self.descripcion_var, width=40).pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Lista de eventos
        lista_frame = ttk.LabelFrame(main_frame, text="Eventos Programados", padding="10")
        lista_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # Treeview
        columnas = ('fecha', 'hora', 'descripcion')
        self.tree = ttk.Treeview(lista_frame, columns=columnas, show='headings', height=12)

        # Configurar columnas
        self.tree.heading('fecha', text='Fecha')
        self.tree.heading('hora', text='Hora')
        self.tree.heading('descripcion', text='Descripción')

        self.tree.column('fecha', width=100)
        self.tree.column('hora', width=80)
        self.tree.column('descripcion', width=400)

        # Scrollbar
        scrollbar = ttk.Scrollbar(lista_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Ubicar treeview y scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Botones
        botones_frame = ttk.Frame(main_frame)
        botones_frame.pack(fill=tk.X)

        ttk.Button(botones_frame, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(botones_frame, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT,
                                                                                                          padx=5,
                                                                                                          pady=5)
        ttk.Button(botones_frame, text="Salir", command=self.salir).pack(side=tk.RIGHT, padx=5, pady=5)

    def agregar_evento(self):
        fecha = self.fecha_var.get()
        hora = self.hora_var.get()
        descripcion = self.descripcion_var.get().strip()

        if not all([fecha, hora, descripcion]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        # Validar formato de fecha y hora
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
            datetime.strptime(hora, '%H:%M')
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora inválido. Use YYYY-MM-DD y HH:MM")
            return

        nuevo_evento = {
            'fecha': fecha,
            'hora': hora,
            'descripcion': descripcion
        }

        self.eventos.append(nuevo_evento)
        self.actualizar_lista_eventos()
        self.guardar_datos()
        self.descripcion_var.set("")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar el evento seleccionado?"):
            index = int(seleccion[0].lstrip('I')) - 1
            del self.eventos[index]
            self.actualizar_lista_eventos()
            self.guardar_datos()

    def actualizar_lista_eventos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        eventos_ordenados = sorted(self.eventos, key=lambda x: (x['fecha'], x['hora']))

        for i, evento in enumerate(eventos_ordenados, 1):
            self.tree.insert('', 'end', iid=f"I{i}",
                             values=(evento['fecha'], evento['hora'], evento['descripcion']))

    def cargar_datos(self):
        self.archivo_datos = "eventos.json"
        self.eventos = []

        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r') as f:
                    self.eventos = json.load(f)
            except:
                pass

    def guardar_datos(self):
        try:
            with open(self.archivo_datos, 'w') as f:
                json.dump(self.eventos, f, indent=2)
        except:
            pass

    def salir(self):
        if messagebox.askyesno("Salir", "¿Está seguro de que desea salir?"):
            self.guardar_datos()
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()