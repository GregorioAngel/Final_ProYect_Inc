#Review: Estructura de la clase:
import json

class Review:
    def __init__(self):
        self.id = None
        self.id_destino = None
        self.id_usuario = None
        self.id_calificacion =  None
        self.comentario = None
        self.animo = None
    
    def Ingresar_informacion(self):
        self.id = int(input("Ingrese su ID de usuario: "))
        self.id_destino = int(input("Ingrese el ID del destino: "))
        self.id_usuario = int(input("Ingrese su ID de usuario: "))
        self.id_calificacion = int(input("Ingrese su calificacíon: "))
        self.comentario = input("Ingrese un comentario: ")
        self.animo = input("Ingrese su estado de ánimo: ")

    def Mostrar_informacion(self):
        print(f"ID de destino: {self.id_destino}")
        print(f"ID de usuario: {self.id_usuario}")
        print(f"Calificacion: {self.id_calificacion}")
        print(f"Comentario: {self.comentario}")
        print(f"Su estado de ánimo: {self.animo}")

    def a_json(self):
        data = {
            "ID de destino": self.id_destino,
            "ID de usuario": self.id_usuario,
            "Calificacion": self.id_calificacion,
            "Comentario": self.comentario,
            "Su estado de animo": self.animo
            }
        return (data)

review_1 = Review()
review_1.Ingresar_informacion()
#review_1.Mostrar_informacion()
datos = json.dumps(review_1.a_json())
print(datos)