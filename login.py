#Importaciones
import tkinter as tk
import customtkinter as ctk
import os
from PIL import ImageTk, Image
from models.usuario import Usuario
from controller.controlador_principal import ControladorPrincipal

# Modo de color y tema
ctk.set_appearance_mode("Sytem")
ctk.set_default_color_theme("blue")

# ---> Rutas
# Carpeta principal del proyecto
carpeta_principal = os.path.dirname(__file__)
# Carpeta de imágenes
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")

# Ventana de Login
class Login:
    def __init__(self):
        # Creación de la ventana principal
        self.root = ctk.CTk() # Instancia
        self.root.title("Ingreso a Food Travel")
        self.root.iconbitmap("views/images/FT.ico")
        self.root.geometry("450x450")

        # Contenido de la ventana principal
        # Logo
        logo = ctk.CTkImage(
            light_image=Image.open("views/images/FT.png"), # Imagen modo claro
            dark_image=Image.open("views/images/FT.png"), # Imagen modo oscuro
            size=(250, 250)) # Tamaño de las imágenes

        #logo = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "logo.png")))
        #ctk.Label(self.root, image=logo).pack()

        etiqueta = ctk.CTkLabel(master=self.root, image=logo, text="")
        etiqueta.pack(pady=15)

        # Campos de texto
        # Usuario
        ctk.CTkLabel(self.root, text="Usuario").pack()
        self.usuario = ctk.CTkEntry(self.root)
        self.usuario.insert(0, "Nombre de usuario")
        self.usuario.bind("<Button-1>", lambda e: self.usuario.delete(0, 'end'))
        self.usuario.pack()

        # Contraseña
        ctk.CTkLabel(self.root, text="Contraseña").pack()
        self.contrasena = ctk.CTkEntry(self.root)
        self.contrasena.insert(0, "*******")
        self.contrasena.bind("<Button-1>", lambda e: self.contrasena.delete(0, 'end'))
        self.contrasena.pack()

        # Botón de envío
        ctk.CTkButton(self.root, text="Entrar", command=self.validar).pack(pady=10)
        # Bucle de ejecución
        self.root.mainloop()
  
    # Función para validar el login
    def validar(self):
        #obtener_usuario = self.usuario.get() # Obtenemos el nombre de usuario
        #obtener_contrasena = self.contrasena.get() # Obtenemos la contraseña
        print("validar")
        self.usuarios = Usuario.cargar_usuarios("data/usuarios.json")
        nrousuarios = len(self.usuarios) 
        id_ = nrousuarios
        nombre_ = self.usuario.get()
        apellido_ = self.contrasena.get()
        historial_ruta_=[]
        #usuario_=Usuario(id_, nombre_, apellido_, historial_ruta_)
        #guardar = "N"
        for i in range(len(self.usuarios)):
            if self.usuarios[i].nombre == nombre_ and self.usuarios[i].apellido == apellido_:
                if hasattr(self, "info_login"):
                    self.info_login.destroy()
                    # Crea esta etiqueta siempre que el login sea correcto
                self. info_login = ctk.CTkLabel(self.root, text=f"Hola, {nombre_}. Espere unos instantes...")
                self.info_login.pack()
                # Se destruye la ventana de login
                self.root.destroy()
                # Se instancia la ventana de opciones
                controlgral = Ventana_Principal()
            else:
               # En caso de tener ya un elemento "info_login" (etiqueta) creado, lo borra
               if hasattr(self, "info_login"):
                    self.info_login.destroy()
                    # Crea esta etiqueta siempre que el login sea incorrecto
               self.info_login = ctk.CTkLabel(self.root, text="Usuario o contraseña incorrectos.")
               self.info_login.pack()


"""
        # Verifica si el valor que tiene el usuario o la contraseña o ambos no coinciden
        if obtener_usuario != acceso_bd["user"] or obtener_contrasena != acceso_bd["password"]:
            # En caso de tener ya un elemento "info_login" (etiqueta) creado, lo borra
            if hasattr(self, "info_login"):
                self.info_login.destroy()
            # Crea esta etiqueta siempre que el login sea incorrecto
            self.info_login = ctk.CTkLabel(self.root, text="Usuario o contraseña incorrectos.")
            self.info_login.pack()
        else:
            # En caso de tener ya un elemento "info_login" (etiqueta) creado, lo borra
            if hasattr(self, "info_login"):
                self.info_login.destroy()
            # Crea esta etiqueta siempre que el login sea correcto
            self. info_login = ctk.CTkLabel(self.root, text=f"Hola, {obtener_usuario}. Espere unos instantes...")
            self.info_login.pack()
            # Se destruye la ventana de login
            self.root.destroy()
            # Se instancia la ventana de opciones
            ventana_opciones = VentanaOpciones()
"""


class Ventana_Principal:

     def __init__(self):
        self.root = tk.Tk()
        self.root.title("Food Travel")
        self.root.geometry("1100x700")
        self.root.iconbitmap("views/images/FT.ico")
        controlador = ControladorPrincipal(self.root)
        self.root.mainloop()

#ventana_login = Login()        