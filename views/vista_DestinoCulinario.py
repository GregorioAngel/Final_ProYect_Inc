#Vista_DestinoCulinario.py
import json
import tkinter as tk
from tkinter import messagebox
from models.DestinoCulinario import DestinoCulinario
from models.local import Local

class VisitasCulinarias:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Destino Culinario")
        self.root.iconbitmap("views/images/FT.ico")

        # Crea los widgets
        label_id = tk.Label(self.root, text="Ingrese el ID:")
        self.entry_id = tk.Entry(self.root)

        label_latitud = tk.Label(self.root, text="Ingrese la latitud:")
        self.entry_latitud = tk.Entry(self.root)

        label_longitud = tk.Label(self.root, text="Ingrese la longitud:")
        self.entry_longitud = tk.Entry(self.root)

        label_direccion = tk.Label(self.root, text="Direccion:")
        self.entry_direccion = tk.Entry(self.root)

        label_nombre = tk.Label(self.root, text="Nombre del lugar:")
        self.entry_nombre = tk.Entry(self.root)

        label_tipo_cocina = tk.Label(self.root, text="Tipo de cocina:")
        self.entry_tipo_cocina = tk.Entry(self.root)

        label_ingredientes = tk.Label(self.root, text="Ingredientes (separados por comas):")
        self.entry_ingredientes = tk.Entry(self.root)

        label_precio_min = tk.Label(self.root, text="Precio mínimo del plato:")
        self.entry_precio_min = tk.Entry(self.root)

        label_precio_max = tk.Label(self.root, text="Precio máximo del plato:")
        self.entry_precio_max = tk.Entry(self.root)

        label_popularidad = tk.Label(self.root, text="Índice de popularidad de (1 a 5):")
        self.entry_popularidad = tk.Entry(self.root)

        label_disponibilidad = tk.Label(self.root, text="Disponibilidad:")
        self.var_disponibilidad = tk.BooleanVar()
        check_disponibilidad = tk.Checkbutton(self.root, text="Disponible", variable=self.var_disponibilidad)

        label_imagen = tk.Label(self.root, text="URL de la imagen:")
        self.entry_imagen = tk.Entry(self.root)

        boton_guardar = tk.Button(self.root, text="Guardar", command=self.guardar_datos)
        boton_mostrar = tk.Button(self.root, text="Mostrar información", command=self.mostrar_informacion)

        # Posiciona los widgets en la ventana
        label_id.grid(row=0, column=0, padx=10, pady=5)
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        label_latitud.grid(row=1, column=0, padx=10, pady=5)
        self.entry_latitud.grid(row=1, column=1, padx=10, pady=5)

        label_longitud.grid(row=2, column=0, padx=10, pady=5)
        self.entry_longitud.grid(row=2, column=1, padx=10, pady=5)

        label_direccion.grid(row=3, column=0, padx=10, pady=5)
        self.entry_direccion.grid(row=3, column=1, padx=10, pady=5)

        label_nombre.grid(row=4, column=0, padx=10, pady=5)
        self.entry_nombre.grid(row=4, column=1, padx=10, pady=5)

        label_tipo_cocina.grid(row=5, column=0, padx=10, pady=5)
        self.entry_tipo_cocina.grid(row=5, column=1, padx=10, pady=5)

        label_ingredientes.grid(row=6, column=0, padx=10, pady=5)
        self.entry_ingredientes.grid(row=6, column=1, padx=10, pady=5)

        label_precio_min.grid(row=7, column=0, padx=10, pady=5)
        self.entry_precio_min.grid(row=7, column=1, padx=10, pady=5)

        label_precio_max.grid(row=8, column=0, padx=10, pady=5)
        self.entry_precio_max.grid(row=8, column=1, padx=10, pady=5)

        label_popularidad.grid(row=9, column=0, padx=10, pady=5)
        self.entry_popularidad.grid(row=9, column=1, padx=10, pady=5)

        label_disponibilidad.grid(row=10, column=0, padx=10, pady=5)
        check_disponibilidad.grid(row=10, column=1, padx=10, pady=5)

        label_imagen.grid(row=11, column=0, padx=10, pady=5)
        self.entry_imagen.grid(row=11, column=1, padx=10, pady=5)

        boton_guardar.grid(row=12, column=0, padx=10, pady=5)
        boton_mostrar.grid(row=12, column=1, padx=10, pady=5)

        # Crea una instancia de la clase DestinoCulinario
        self.destino_1 = DestinoCulinario()

    def guardar_datos(self):

        # Solo obtenemos los campos necesarios del formulario
        nombre = self.entry_nombre.get()
        imagen = "image_3.png" #self.entry_imagen.get()
        id_destino = self.entry_id.get()

        # Creamos un objeto Local con los datos capturados
        local = Local(nombre, imagen, id_destino)

        # Guardamos los datos en locales.json
        with open("data/locales.json", "r") as archivo:
            datos_locales = json.load(archivo)

        datos_locales.append(json.loads(local.a_json()))

        with open("data/locales.json", "w") as archivo:
            json.dump(datos_locales, archivo, indent=4)

        self.destino_1.Ingresar_informacion(
            self.entry_id.get(),
            self.entry_latitud.get(),
            self.entry_longitud.get(),
            self.entry_direccion.get(),
            self.entry_nombre.get(),
            self.entry_tipo_cocina.get(),
            self.entry_ingredientes.get(),
            self.entry_precio_min.get(),
            self.entry_precio_max.get(),
            self.entry_popularidad.get(),
            self.var_disponibilidad.get(),
            self.entry_imagen.get()
        )

        self.destino_1.guardar_datos()
        messagebox.showinfo("Guardado", "Los datos se han guardado correctamente.")
        self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_latitud.delete(0, tk.END)
        self.entry_longitud.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_tipo_cocina.delete(0, tk.END)
        self.entry_ingredientes.delete(0, tk.END)
        self.entry_precio_min.delete(0, tk.END)
        self.entry_precio_max.delete(0, tk.END)
        self.entry_popularidad.delete(0, tk.END)
        self.entry_imagen.delete(0, tk.END)

    def mostrar_informacion(self):
        self.destino_1.Ingresar_informacion(
            self.entry_id.get(),
            self.entry_latitud.get(),
            self.entry_longitud.get(),
            self.entry_direccion.get(),
            self.entry_nombre.get(),
            self.entry_tipo_cocina.get(),
            self.entry_ingredientes.get(),
            self.entry_precio_min.get(),
            self.entry_precio_max.get(),
            self.entry_popularidad.get(),
            self.var_disponibilidad.get(),
            self.entry_imagen.get()
        )

        messagebox.showinfo("Información", self.destino_1.Mostrar_Informacion())

    def run(self):
        self.root.mainloop()