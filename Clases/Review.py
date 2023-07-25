import tkinter as tk
import json

class Review:
    def __init__(self):
        #self.id = None
        self.id_destino = None
        self.id_usuario = None
        self.id_calificacion = None
        self.comentario = None
        self.animo = None

    def Ingresar_informacion(self):
        #self.id = ""
        self.id_destino = int(entry_destino.get())
        self.id_usuario = int(entry_usuario.get())
        self.id_calificacion = int(entry_calificacion.get())
        self.comentario = entry_comentario.get()
        self.animo = entry_animo.get()

        # Mostrar la información en la ventana
        self.Mostrar_informacion()

    def Mostrar_informacion(self):
        info_text.set(f"ID de destino: {self.id_destino}\n"
                      f"ID de usuario: {self.id_usuario}\n"
                      f"Calificación: {self.id_calificacion}\n"
                      f"Comentario: {self.comentario}\n"
                      f"Su estado de ánimo: {self.animo}")

    def a_json(self):
        data = {
            "ID de destino": self.id_destino,
            "ID de usuario": self.id_usuario,
            "Calificación": self.id_calificacion,
            "Comentario": self.comentario,
            "Su estado de ánimo": self.animo
        }
        return data

# Función para guardar la información en un archivo JSON
def guardar_json():
    review = Review()
    review.Ingresar_informacion()
    datos = json.dumps(review.a_json(), indent=4)

    with open("review.json", "w") as file:
        file.write(datos)
    
    info_text.set("Datos guardados en review.json")

# Crear ventana principal
root = tk.Tk()
root.title("Sección de Reviews")

# Etiquetas y campos de entrada
label_destino = tk.Label(root, text="Ingrese el ID del destino:")
label_destino.grid(row=0, column=0, padx=5, pady=5)
entry_destino = tk.Entry(root)
entry_destino.grid(row=0, column=1, padx=5, pady=5)

label_usuario = tk.Label(root, text="Ingrese su ID de usuario:")
label_usuario.grid(row=1, column=0, padx=5, pady=5)
entry_usuario = tk.Entry(root)
entry_usuario.grid(row=1, column=1, padx=5, pady=5)

label_calificacion = tk.Label(root, text="Ingrese su calificación:")
label_calificacion.grid(row=2, column=0, padx=5, pady=5)
entry_calificacion = tk.Entry(root)
entry_calificacion.grid(row=2, column=1, padx=5, pady=5)

label_comentario = tk.Label(root, text="Ingrese un comentario:")
label_comentario.grid(row=3, column=0, padx=5, pady=5)
entry_comentario = tk.Entry(root)
entry_comentario.grid(row=3, column=1, padx=5, pady=5)

label_animo = tk.Label(root, text="Ingrese su estado de ánimo:")
label_animo.grid(row=4, column=0, padx=5, pady=5)
entry_animo = tk.Entry(root)
entry_animo.grid(row=4, column=1, padx=5, pady=5)

# Botón para guardar los datos
save_button = tk.Button(root, text="Guardar", command=guardar_json)
save_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

# Texto para mostrar la información ingresada
info_text = tk.StringVar()
info_label = tk.Label(root, textvariable=info_text)
info_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()