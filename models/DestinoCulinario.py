# DestinoCulinario.py
import json
import os

class DestinoCulinario:
    def __init__(self):
        self.id = None
        self.latitud = None
        self.longitud = None
        self.direccion = None
        self.nombre = None
        self.tipo_cocina = None
        self.ingredientes = None
        self.precio_minimo = None
        self.precio_maximo = None
        self.popularidad = None
        self.disponibilidad = None
        self.imagen = None

    def Ingresar_informacion(self, id, latitud, longitud, direccion, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo,
                             popularidad, disponibilidad, imagen):
        self.id = int(id)
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = direccion
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes.split(",")
        self.precio_minimo = float(precio_minimo)
        self.precio_maximo = float(precio_maximo)
        self.popularidad = float(popularidad)
        self.disponibilidad = disponibilidad
        self.imagen = imagen

    def Mostrar_Informacion(self):
        return f"ID: {self.id}\n" \
               f"Latitud: {self.latitud}\n" \
               f"Longitud: {self.longitud}\n" \
               f"Direccion: {self.direccion}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Tipo de cocina: {self.tipo_cocina}\n" \
               f"Ingredientes: {', '.join(self.ingredientes)}\n" \
               f"Precio mínimo: {self.precio_minimo}\n" \
               f"Precio máximo: {self.precio_maximo}\n" \
               f"Popularidad: {self.popularidad}\n" \
               f"Disponibilidad: {'Disponible' if self.disponibilidad else 'No disponible'}\n" \
               f"Imagen: {self.imagen}"

    def guardar_datos(self):
        datos = {
            "id": int(self.id),
            "latitud": float(self.latitud),
            "longitud": float(self.longitud),
            "direccion": self.direccion,
            "nombre": self.nombre,
            "tipo_cocina": self.tipo_cocina,
            "ingredientes": self.ingredientes,
            "precio_minimo": self.precio_minimo,
            "precio_maximo": self.precio_maximo,
            "popularidad": self.popularidad,
            "disponibilidad": 'Disponible' if self.disponibilidad else 'No disponible',
            "imagen": "image_3.png",
        }
        # Modificacion de ingreso de Json
        #Guarda los datos en ubicaciones.json
        #file_path = r'F:\Cosas\Cristian\Microsoft VS Code Trabajos\Proyecto-Final-Python\Final_ProYect_Inc\Data\ubicaciones.json'

        #if os.path.exists(file_path):
        if os.path.exists("data/ubicaciones.json"):     
            with open("data/ubicaciones.json", 'r') as file:
                data = json.load(file)
        else:
            data = []

        data.append(datos)

        #with open(file_path, 'w') as file:
        with open("data/ubicaciones.json", 'w') as file:
             json.dump(data, file, indent=4)
        
