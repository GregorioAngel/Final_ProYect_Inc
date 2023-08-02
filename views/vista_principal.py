#vista principal.py
import tkinter as tk
#from tkinter import ttk
from tkinter import messagebox
from tkintermapview import TkinterMapView
#from PIL import Image, ImageTk
from models.usuario import Usuario
import json
from views.vista_DestinoCulinario import VisitasCulinarias

class VistaPrincipal:
    def __init__(self, root, seleccionar_local_callback=None, seleccionar_DestinoCulinario_callback=None):
        self.root = root
        self.seleccionar_local_callback = seleccionar_local_callback
        self.seleccionar_DestinoCulinario_callback = seleccionar_DestinoCulinario_callback
       
        #comienza dibujo pantalla
        self.frame_top = tk.Frame(self.root, padx=5, pady=1)
        self.frame_top.pack(side='top', fill='x')
        titulo = tk.Label(self.frame_top, text="Welcome to Food Travel", font=("Wide Latin", 23))
        titulo.pack(pady=40 , padx=20)

        self.frame_locales = tk.Frame(self.root, width=400, height=300)
        self.frame_locales.pack(side='left', fill='both', expand=False, padx=10, pady=0)

        self.frame_mapa = tk.Frame(self.root, width=600, height=600)
        self.frame_mapa.pack(side='left')

        # Placeholder para el mapa
        self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-24.7858636034, -65.408408504006)  
        self.mapa.set_zoom(16)
        self.mapa.pack(side='right')

        # Listbox para los locales
        self.lista_locales = tk.Listbox(self.frame_locales)
        self.lista_locales.bind('<<ListboxSelect>>', seleccionar_local_callback)
        self.lista_locales.pack(fill='both', expand=True)
        # Crear un frame para centrar el botón y una etiqueta de bienvenida
        frame_centro = tk.Frame(self.root)
        frame_centro.pack(expand=True, fill=tk.BOTH)

        label_bienvenida= tk.Label(frame_centro, text="Bienvenido a nuestra App Culinaria", font=("Arial", 16))
        label_bienvenida.pack(pady=30)

        boton_abrir_visitas_culinarias = tk.Button(frame_centro, text="Visitas Culinarias", command=VisitasCulinarias)
        boton_abrir_visitas_culinarias.pack(pady=50)

    def agregar_local(self, local):
        nombre = local.nombre
        self.lista_locales.insert(tk.END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_DestinoCulinario_callback)

