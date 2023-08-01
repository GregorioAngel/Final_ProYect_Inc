#main.py
import tkinter as tk
from PIL import Image, ImageTk
from controller.controlador_principal import ControladorPrincipal
from views.vista_DestinoCulinario import VisitasCulinarias
from tkinter import messagebox


def abrir_ventana_visitas_culinarias():
    formulario = VisitasCulinarias()

root = tk.Tk()
root.title("Food Travel")
root.geometry("1100x700")
root.iconbitmap("views/images/FT.ico")
controlador = ControladorPrincipal(root)


# Este codigo pone al boton abajo del cuadro de usuario.
#boton_abrir_visitas_culinarias = tk.Button(root, text="Destino Culinario", command=abrir_ventana_visitas_culinarias)
#boton_abrir_visitas_culinarias.pack()


# Crear un frame para centrar el botón y una etiqueta de bienvenida
frame_centro = tk.Frame(root)
frame_centro.pack(expand=True, fill=tk.BOTH)

label_bienvenida= tk.Label(frame_centro, text="Bienvenido a nuestra App Culinaria", font=("Arial", 16))
label_bienvenida.pack(pady=30)

boton_abrir_visitas_culinarias = tk.Button(frame_centro, text="Visitas Culinarias", command=abrir_ventana_visitas_culinarias)
boton_abrir_visitas_culinarias.pack(pady=50)

def mostrar_eventos():
    # Obtener el índice de la ubicación seleccionada
    indice_seleccionado = controlador.vista.lista_locales.curselection()
    if not indice_seleccionado:
        messagebox.showinfo("Error", "Por favor, seleccione una ubicación antes de ver los eventos.")
        return

    # Obtener el id_DestinoCulinario de la ubicación seleccionada
    id_destino_culinario = controlador.locales[indice_seleccionado[0]].id_DestinoCulinario
    controlador.vista.mostrar_eventos(id_destino_culinario)

boton_abrir_eventos = tk.Button(frame_centro, text="Eventos", command=mostrar_eventos)
boton_abrir_eventos.pack(pady=10)

root.mainloop()
