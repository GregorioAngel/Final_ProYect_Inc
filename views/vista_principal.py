#vista principal.py
import tkinter as tk
#from tkinter import ttk
from tkintermapview import TkinterMapView
#from PIL import Image, ImageTk

class VistaPrincipal:
    def __init__(self, root, seleccionar_local_callback=None, seleccionar_DestinoCulinario_callback=None):
        self.root = root
        self.seleccionar_local_callback = seleccionar_local_callback
        self.seleccionar_DestinoCulinario_callback = seleccionar_DestinoCulinario_callback
       
        #comienza dibujo pantalla
        self.frame_top = tk.Frame(self.root, padx=5, pady=1)
        self.frame_top.pack(side='top', fill='x')
        titulo = tk.Label(self.frame_top, text="Food Travel", font=("Wide Latin", 20))
        titulo.pack(side='left', padx=20)

        r_frame = tk.LabelFrame(self.frame_top, text="Ingrese Usuario")
        r_frame.pack(side='right', fill='y')

        # Crear un frame para agrupar los entrys y el botón horizontalmente
        entry_boton_frame = tk.Frame(r_frame)
        entry_boton_frame.pack(padx=10, pady=5)

        label = tk.Label(entry_boton_frame, text="Nombre", font=("Arial", 11))
        label.pack(side='left', pady=1)
        nombre = tk.Entry(entry_boton_frame)
        nombre.pack(fill='x', side='left', padx=5, pady=5)

        label2 = tk.Label(entry_boton_frame, text="Contraseña", font=("Arial", 11))
        label2.pack(side='left', pady=1)
        apellido = tk.Entry(entry_boton_frame)
        apellido.pack(fill='x', side='left', padx=5, pady=5)

        # Agregar el botón "Ingresar"
        boton_ingresar = tk.Button(r_frame, text="Ingresar")
        boton_ingresar.pack(pady=5)

        self.frame_locales = tk.Frame(self.root, width=400, height=300)
        self.frame_locales.pack(side='left', fill='both', expand=False, padx=10, pady=0)

        self.frame_mapa = tk.Frame(self.root, width=600, height=600)
        self.frame_mapa.pack(side='left')

        # Placeholder para el mapa
        self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.pack(side='right')

        # Listbox para los locales
        self.lista_locales = tk.Listbox(self.frame_locales)
        self.lista_locales.bind('<<ListboxSelect>>', seleccionar_local_callback)
        self.lista_locales.pack(fill='both', expand=True)

    def agregar_local(self, local):
        nombre = local.nombre
        self.lista_locales.insert(tk.END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_DestinoCulinario_callback)


