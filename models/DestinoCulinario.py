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
            "ID": self.id,
            "Latitud": self.latitud,
            "Longitud": self.longitud,
            "Direccion": self.direccion,
            "Nombre": self.nombre,
            "Tipo de cocina": self.tipo_cocina,
            "Ingredientes": self.ingredientes,
            "Precio minimo": self.precio_minimo,
            "Precio maximo": self.precio_maximo,
            "Popularidad": self.popularidad,
            "Disponibilidad": 'Disponible' if self.disponibilidad else 'No disponible',
            "Imagen": self.imagen,
        }
        #Guarda los datos en ubicaciones.json
        file_path = r'F:\Cosas\Cristian\Microsoft VS Code Trabajos\Proyecto-Final-Python\Final_ProYect_Inc\Data\ubicaciones.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
        else:
            data = []

        data.append(datos)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)


        # Guarda los datos en local.json
        # file_path_2 = r'F:\Cosas\Cristian\Microsoft VS Code Trabajos\Proyecto-Final-Python\Final_ProYect_Inc\Data\locales.json'

        # if os.path.exists(file_path_2):
        #     with open(file_path_2, 'r') as file:
        #         data = json.load(file)
        # else:
        #     data = []

        # data.append(datos)

        # with open(file_path_2, 'w') as file:
        #     json.dump(data, file, indent=4)

