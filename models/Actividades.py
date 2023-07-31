import json

#CLASE

class Actividad:

    def __init__(self, id, nombre, destino_id, hora_inicio):
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio

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
#---------------------------------------------------------
# Este es un ejemplo mio para ver que funcione, aca vendria el vinculo con los archivos .json
#REVISAR
actividad = Actividad(2,"los nocheros", 5, "2023-07-29T21:00:00")

print(actividad)

#---------------------------------------------------------
# INSTANCIACION DEL OBJETO PYTHON

actividad_json = json.dumps(actividad.a_json(), indent=4)

print(actividad_json)
