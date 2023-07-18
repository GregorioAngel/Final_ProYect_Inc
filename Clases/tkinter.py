# Ejemplo de uso
restaurante = 'Restaurante Ejemplo'
direccion = 'Calle de ejemplo, 123'
coordenadas = {'latitud': 40.7128, 'longitud': -74.0060}

ubicacion = Ubicacion(restaurante, direccion, coordenadas)
ubicacion_json = ubicacion.to_json()
print(ubicacion_json)

import folium
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
import webbrowser

def open_map_in_browser():
    # Coordenadas de Cafayate
    latitud = -26.0733
    longitud = -65.9762

    # Crear un objeto de mapa centrado en Cafayate
    mapa_cafayate = folium.Map(location=[latitud, longitud], zoom_start=14)

    # Agregar un marcador en Cafayate
    folium.Marker(location=[latitud, longitud], popup='Cafayate, Salta').add_to(mapa_cafayate)

    # Convertir el mapa de Folium a una imagen
    tmpfile = BytesIO()
    mapa_cafayate.save(tmpfile, close_file=False)
    tmpfile.seek(0)
    img = Image.open(tmpfile)

    # Mostrar el mapa en la interfaz gráfica
    map_img = ImageTk.PhotoImage(img)
    map_label.configure(image=map_img)
    map_label.image = map_img

def open_in_browser():
    webbrowser.open('cafayate_mapa.html')

if __name__ == "__main__":
    # Crear ventana
    root = tk.Tk()
    root.title("Mapa de Cafayate")

    # Crear contenedor para el mapa
    map_frame = ttk.Frame(root)
    map_frame.pack()

    # Etiqueta para mostrar el mapa
    map_label = ttk.Label(map_frame)
    map_label.pack()

    # Botón para abrir el mapa en el navegador
    open_in_browser_button = ttk.Button(root, text="Abrir en el navegador", command=open_in_browser)
    open_in_browser_button.pack()

    # Botón para actualizar el mapa
    update_map_button = ttk.Button(root, text="Actualizar mapa", command=open_map_in_browser)
    update_map_button.pack()

    # Cargar el mapa por defecto al abrir la aplicación
    open_map_in_browser()

    # Ejecutar la aplicación
    root.mainloop()
