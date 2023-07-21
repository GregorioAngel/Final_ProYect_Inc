#Destino Culinario: Estructura de la clase:
import json

class DestinoCulinario:
    def __init__(self):
        #self.id = None
        self.nombre = None
        self.tipo_cocina = None
        self.ingredientes = None
        self.precio_minimo = None
        self.precio_maximo = None
        self.popularidad = None
        self.disponibilidad = None
        self.id_ubicacion = None
        self.imagen = None

    def Ingresar_informacion(self):
        #self.id = int(input("Igrese su ID de usuario: "))
        self.nombre = input("Ingrese el nombre del lugar: ")
        self.tipo_cocina = input("Ingrese el tipo de cocina que busca: ")
        self.ingredientes = input("Ingrese los ingredientes separadas por comas: ").split(",")
        self.precio_minimo = float(input("Ingrese el precio mínimo del plato: "))
        self.precio_maximo = float(input("Ingrese el precio máximo del plato: "))
        self.popularidad = float(input("Ingrese el índice de popularidad: "))
        self.disponibilidad = input("Ingresa la disponibilidad (Si/No)").lower() == "si"
        self.id_ubicacion = int(input("Ingrese el ID de la ubicación: "))
        #self.id_fecha = int(input("Ingrese la fecha: "))
        self.imagen = input("Ingrese el URL de la imagen: ")


    def Mostrar_Informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tipo de cocina: {self.tipo_cocina}")
        print(f"Ingredientes: {self.ingredientes}")
        print(f"Precio mínimo: {self.precio_minimo}")
        print(f"Precio máximo: {self.precio_maximo}")
        print(f"Popularidad: {self.popularidad}")
        print(f"Disponibilidad: {'Disponible' if self.disponibilidad else 'No disponible'}")
        print(f"ID de la ubicación: {self.id_ubicacion}")
        print(f"Imagen: {self.imagen}")

    def a_json(self):
        data = {
            "Nombre": self.nombre,
            "Tipo de cocina": self.tipo_cocina,
            "Ingredientes": self.ingredientes,
            "Precio minimo": self.precio_minimo,
            "Precio maximo": self.precio_maximo,
            "Popularidad": self.popularidad,
            "Dispnibilidad": 'Disponible' if self.disponibilidad else 'No disponible',
            "ID de la ubicacion": self.id_ubicacion,
            "Imagen": self.imagen,
            }
        return (data)

destino_1 = DestinoCulinario()
destino_1.Ingresar_informacion()
#destino_1.Mostrar_Informacion()
datos = json.dumps(destino_1.a_json(), indent=4)
print(datos)

