import tkinter as tk

# Función para mostrar los detalles de la actividad en el cuadro de texto
def mostrar_detalles():
    detalles_json = json.dumps(actividad.a_json(), indent=4)
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, detalles_json)

# Ventana principal
root = tk.Tk()
root.title("Detalles de su Actividad")

# Cuadro de texto
text_box = tk.Text(root, width=50, height=10)
text_box.pack()

#Botón para mostrar los detalles de la Actividad
boton_mostrar = tk.Button(root, text="Mostrar Detalles", command=mostrar_detalles, height=2, width=20, font=("Arial", 12))
boton_mostrar.pack()



root.mainloop()
