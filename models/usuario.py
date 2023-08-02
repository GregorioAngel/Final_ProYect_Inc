import json

class Usuario:
    def __init__(self, id, nombre, apellido, historial_ruta):
        self.id=id
        self.nombre = nombre
        self.apellido=apellido
        self.historial_ruta = historial_ruta

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
        return [Usuario.de_json(json.dumps(dato)) for dato in datos]