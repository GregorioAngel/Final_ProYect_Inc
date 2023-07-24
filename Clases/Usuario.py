#Clase Usuarios
import json

class Usuarios:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.id = 0

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_usuarios(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Usuarios.de_json(json.dumps(dato)) for dato in datos]