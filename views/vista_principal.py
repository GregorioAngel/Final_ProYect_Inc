#vista principal.py
import tkinter as tk
#from tkinter import ttk
from tkinter import messagebox
from tkintermapview import TkinterMapView
#from PIL import Image, ImageTk
from models.usuario import Usuario
import json

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
        self.nombre = tk.Entry(entry_boton_frame)
        self.nombre.pack(fill='x', side='left', padx=5, pady=5)

        label2 = tk.Label(entry_boton_frame, text="Apellido", font=("Arial", 11))
        label2.pack(side='left', pady=1)
        self.apellido = tk.Entry(entry_boton_frame)
        self.apellido.pack(fill='x', side='left', padx=5, pady=5)

        # Agregar el botón "Ingresar"
        boton_ingresar = tk.Button(r_frame, text="   I n g r e s a r   " , command=self.guarda_usuario)
        boton_ingresar.pack(side='right', padx=30, pady=5)

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

    def guarda_usuario(self):
        ##################################################
        # Solo obtenemos los campos necesarios del formulario
        # Creamos un objeto Local con los datos capturados
        self.usuarios = Usuario.cargar_usuarios("data/usuarios.json")
        nrousuarios = len(self.usuarios)

        id_ = nrousuarios
        nombre_ = self.nombre.get()
        apellido_ = self.apellido.get()
        historial_ruta_=[]
        usuario_=Usuario(id_, nombre_, apellido_, historial_ruta_)
        guardar = "N"
        for i in range(len(self.usuarios)):
            if self.usuarios[i].nombre == nombre_ and self.usuarios[i].apellido == apellido_:
               # messagebox.showinfo("Usuario encontrado")        
                break
            else:
                guardar = "S"

        if guardar == "S":
             # Guardamos los datos en locales.json
             with open("data/usuarios.json", "r") as archivo:
                  datos_locales = json.load(archivo)

             datos_locales.append(json.loads(usuario_.a_json()))

             with open("data/usuarios.json", "w") as archivo:
                 json.dump(datos_locales, archivo, indent=4)

             # Busca la ubicación correspondiente al local seleccionado
        
             messagebox.showinfo("Guardado", "Los datos del usuario fueron registrados.")
 
        self.apellido.delete(0, tk.END)
        self.nombre.delete(0, tk.END)

        #frame_centro = tk.Frame(self.root)
        #frame_centro.pack(expand=True, fill=tk.BOTH)
        label_usuario= tk.Label(self.root, text=nombre_+" "+apellido_, font=("Arial", 16))
        label_usuario.pack(pady=200)
        #etiqueta = tk.Label(ventana, text="")
        label_usuario.place(x=800, y=60)
     
    #####################################################

    def agregar_local(self, local):
        nombre = local.nombre
        self.lista_locales.insert(tk.END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_DestinoCulinario_callback)


    def mostrar_eventos(self, id_DestinoCulinario):
        eventos = []
        with open("Data/actividades.json", "r") as archivo:
            eventos = json.load(archivo)

        eventos_relacionados = [evento for evento in eventos if evento["id_DestinoCulinario"] == id_DestinoCulinario]

        if not eventos_relacionados:
            messagebox.showinfo("Eventos", "No hay eventos relacionados con esta ubicación.")
            return

        ventana_eventos = tk.Toplevel(self.root)
        ventana_eventos.title("Eventos")
        ventana_eventos.geometry("600x200")

        lista_eventos = tk.Listbox(ventana_eventos, selectmode=tk.SINGLE, font=10)
        lista_eventos.pack(fill='both', expand=True)

        for evento in eventos_relacionados:
            lista_eventos.insert(tk.END, evento["nombre"] + " - Hora: " + evento["hora_inicio"])

        ventana_eventos.mainloop()