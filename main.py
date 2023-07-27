import tkinter as tk
from PIL import Image, ImageTk
from controller.controlador_principal import ControladorPrincipal

root = tk.Tk()
root.title("Food Travel")
root.geometry("1100x700")
root.iconbitmap("views/images/FT.ico")
controlador = ControladorPrincipal(root)
root.mainloop()
