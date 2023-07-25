import json
import tkinter as tk
from tkinter import messagebox


class DestinoCulinario:
    def __init__(self):
        self.nombre = None
        self.tipo_cocina = None
        self.ingredientes = None
        self.precio_minimo = None
        self.precio_maximo = None
        self.popularidad = None
        self.disponibilidad = None
        self.id_ubicacion = None
        self.imagen = None

    def Ingresar_informacion(self):
        self.nombre = entry_nombre.get()
        self.tipo_cocina = entry_tipo_cocina.get()
        self.ingredientes = entry_ingredientes.get().split(",")
        self.precio_minimo = float(entry_precio_min.get())
        self.precio_maximo = float(entry_precio_max.get())
        self.popularidad = float(entry_popularidad.get())
        self.disponibilidad = var_disponibilidad.get()
        self.id_ubicacion = int(entry_id_ubicacion.get())
        self.imagen = entry_imagen.get()

    def Mostrar_Informacion(self):
        messagebox.showinfo("Información", f"Nombre: {self.nombre}\n"
                                            f"Tipo de cocina: {self.tipo_cocina}\n"
                                            f"Ingredientes: {', '.join(self.ingredientes)}\n"
                                            f"Precio mínimo: {self.precio_minimo}\n"
                                            f"Precio máximo: {self.precio_maximo}\n"
                                            f"Popularidad: {self.popularidad}\n"
                                            f"Disponibilidad: {'Disponible' if self.disponibilidad else 'No disponible'}\n"
                                            f"ID de la ubicación: {self.id_ubicacion}\n"
                                            f"Imagen: {self.imagen}")

def guardar_datos():
    # Obtener los datos ingresados por el usuario de los campos de entrada de Tkinter
    nombre = entry_nombre.get()
    tipo_cocina = entry_tipo_cocina.get()
    ingredientes = entry_ingredientes.get().split(",")
    precio_minimo = float(entry_precio_min.get())
    precio_maximo = float(entry_precio_max.get())
    popularidad = float(entry_popularidad.get())
    disponibilidad = var_disponibilidad.get()
    id_ubicacion = int(entry_id_ubicacion.get())
    imagen = entry_imagen.get()

    # Crear un diccionario con los datos obtenidos
    datos = {
        "Nombre": nombre,
        "Tipo de cocina": tipo_cocina,
        "Ingredientes": ingredientes,
        "Precio minimo": precio_minimo,
        "Precio maximo": precio_maximo,
        "Popularidad": popularidad,
        "Disponibilidad": 'Disponible' if disponibilidad else 'No disponible',
        "ID de la ubicacion": id_ubicacion,
        "Imagen": imagen,
    }

    # Guardar el diccionario en un archivo JSON
    with open('destino_culinario.json', 'w') as file:
        json.dump(datos, file, indent=4)

    messagebox.showinfo("Guardado", "Los datos se han guardado correctamente.")

def mostrar_informacion():
    destino_1.Ingresar_informacion()
    destino_1.Mostrar_Informacion()

# Crear la ventana principal
root = tk.Tk()
root.title("Destino Culinario")

# Crear los widgets
label_nombre = tk.Label(root, text="Nombre del lugar:")
entry_nombre = tk.Entry(root)

label_tipo_cocina = tk.Label(root, text="Tipo de cocina:")
entry_tipo_cocina = tk.Entry(root)

label_ingredientes = tk.Label(root, text="Ingredientes (separados por comas):")
entry_ingredientes = tk.Entry(root)

label_precio_min = tk.Label(root, text="Precio mínimo del plato:")
entry_precio_min = tk.Entry(root)

label_precio_max = tk.Label(root, text="Precio máximo del plato:")
entry_precio_max = tk.Entry(root)

label_popularidad = tk.Label(root, text="Índice de popularidad:")
entry_popularidad = tk.Entry(root)

label_disponibilidad = tk.Label(root, text="Disponibilidad:")
var_disponibilidad = tk.BooleanVar()
check_disponibilidad = tk.Checkbutton(root, text="Disponible", variable=var_disponibilidad)

label_id_ubicacion = tk.Label(root, text="ID de la ubicación:")
entry_id_ubicacion = tk.Entry(root)

label_imagen = tk.Label(root, text="URL de la imagen:")
entry_imagen = tk.Entry(root)

boton_guardar = tk.Button(root, text="Guardar", command=guardar_datos)
boton_mostrar = tk.Button(root, text="Mostrar información", command=mostrar_informacion)

# Posicionar los widgets en la ventana
label_nombre.grid(row=0, column=0, padx=10, pady=5)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_tipo_cocina.grid(row=1, column=0, padx=10, pady=5)
entry_tipo_cocina.grid(row=1, column=1, padx=10, pady=5)

label_ingredientes.grid(row=2, column=0, padx=10, pady=5)
entry_ingredientes.grid(row=2, column=1, padx=10, pady=5)

label_precio_min.grid(row=3, column=0, padx=10, pady=5)
entry_precio_min.grid(row=3, column=1, padx=10, pady=5)

label_precio_max.grid(row=4, column=0, padx=10, pady=5)
entry_precio_max.grid(row=4, column=1, padx=10, pady=5)

label_popularidad.grid(row=5, column=0, padx=10, pady=5)
entry_popularidad.grid(row=5, column=1, padx=10, pady=5)

label_disponibilidad.grid(row=6, column=0, padx=10, pady=5)
check_disponibilidad.grid(row=6, column=1, padx=10, pady=5)

label_id_ubicacion.grid(row=7, column=0, padx=10, pady=5)
entry_id_ubicacion.grid(row=7, column=1, padx=10, pady=5)

label_imagen.grid(row=8, column=0, padx=10, pady=5)
entry_imagen.grid(row=8, column=1, padx=10, pady=5)

boton_guardar.grid(row=9, column=0, padx=10, pady=5)
boton_mostrar.grid(row=9, column=1, padx=10, pady=5)

# Crear una instancia de la clase DestinoCulinario
destino_1 = DestinoCulinario()

# Iniciar el bucle principal de Tkinter
root.mainloop()