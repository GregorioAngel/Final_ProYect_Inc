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
        self.locales = []  # Lista de locales
        self.cargar_locales()
       
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

        # Botón para mostrar eventos
        boton_eventos = tk.Button(self.frame_locales, text="Eventos", command=self.mostrar_eventos)
        boton_eventos.pack(side='bottom', pady=10)

    def agregar_local(self, local):
        nombre = local.nombre
        self.lista_locales.insert(tk.END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_DestinoCulinario_callback)

    def cargar_locales(self):
        # Cargar los locales desde el archivo JSON y agregarlos a la lista 'locales'
        with open("data/locales.json", "r") as archivo:
            self.locales = json.load(archivo)

    def mostrar_eventos(self):
        indice_seleccionado = self.lista_locales.curselection()
        if not indice_seleccionado:
            messagebox.showinfo("Error", "Seleccione una ubicación antes de ver los eventos.")
            return

        local_seleccionado = self.locales[indice_seleccionado[0]]
        eventos = []

        with open("data/actividades.json", "r") as archivo:
            actividades = json.load(archivo)

        for actividad in actividades:
            if actividad["id_DestinoCulinario"] == local_seleccionado["id_DestinoCulinario"]:
                eventos.append(actividad["nombre"])

        if eventos:
            mensaje = "\n".join(eventos)
        else:
            mensaje = "No hay eventos para esta ubicación."

        messagebox.showinfo("Eventos", mensaje)