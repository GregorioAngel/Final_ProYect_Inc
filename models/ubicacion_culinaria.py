import json


class Ubicacion_Culinaria:
    def __init__(self, id, latitud, longitud, direccion, nombre, tipo_cocina, ingredientes,precio_minimo, precio_maximo, popularidad, disponibilidad, imagen):
        self.id = id
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = direccion
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.imagen = imagen

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_ubicaciones(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Ubicacion_Culinaria.de_json(json.dumps(dato)) for dato in datos]