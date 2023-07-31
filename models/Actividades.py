import json
import datetime

#CLASE

class Actividad:

    def __init__(self, id, nombre, destino_id, hora_inicio):
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = datetime.datetime.now().isoformat()

    def __str__(self):
        return f"El destino que seleccionaste es el {self.id}, se llama {self.nombre}, esta ubicado en {self.destino_id} e inicia a las {self.hora_inicio}"
 
    def a_json(self):
        return{
            "tipo" : "Actividad",
            "id" : self.id,
            "nombre" : self.nombre,
            "destino_id" : self.destino_id,
            "hora_inicio" : self.hora_inicio
        }
    
    @classmethod
    def cargar_de_json(cls, actividades):
        with open(actividades, "r") as f:
            data = json.load(f)
        return [cls(**actividad) for actividad in data]

