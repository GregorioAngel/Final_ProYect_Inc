#controlador principal.py
from views.vista_principal import VistaPrincipal
from models.local import Local
from models.ubicacion_culinaria import Ubicacion_Culinaria
from PIL import Image, ImageTk

class ControladorPrincipal:
    def __init__(self, root):
        self.vista = VistaPrincipal(root, self.seleccionar_local, seleccionar_DestinoCulinario)
        self.locales = Local.cargar_locales("data/locales.json")
        self.ubicaciones = Ubicacion_Culinaria.cargar_ubicaciones("data/ubicaciones.json")
        self.marcadores = []
        self.imagenes = []
        #nroubicaciones = len(self.ubicaciones) 

        self.cargar_locales()
        self.cargar_imagenes()
        self.cargar_marcadores()
        #print(f"Nro de Ubicación {nroubicaciones}" )
            
    def cargar_locales(self):
        for local in self.locales:
            self.vista.agregar_local(local)
        
    def cargar_imagenes(self):
        for local in self.locales:
            imagen = ImageTk.PhotoImage(Image.open(f"views/images/{local.imagen}").resize((100, 100)))
            self.imagenes.append(imagen)

    def cargar_marcadores(self):
        for destinoCulinario, local in zip(self.ubicaciones, self.locales):
            imagen = self.imagenes[destinoCulinario.id - 1]
            marcador = self.vista.agregar_marcador_mapa(destinoCulinario.latitud, destinoCulinario.longitud, local.nombre, imagen)
            marcador.hide_image(True)
            self.marcadores.append(marcador)

    def seleccionar_local(self, event):
        # Obtiene el índice del elemento seleccionado
        indice_seleccionado = self.vista.lista_locales.curselection()
        # Obtiene el local seleccionado
        local_seleccionado = self.locales[indice_seleccionado[0]]
        
        DestinoCulinario_seleccionada = Ubicacion_Culinaria(0, 0, 0,"","","","","","","","","")
        
        # Busca la ubicación correspondiente al local seleccionado
        for destinoCulinario in self.ubicaciones:
            if destinoCulinario.id == local_seleccionado.id_DestinoCulinario:
                DestinoCulinario_seleccionada = destinoCulinario
                break
        
        # Centra el mapa en la ubicación seleccionada
        self.vista.mapa.set_position(DestinoCulinario_seleccionada.latitud, DestinoCulinario_seleccionada.longitud)

def seleccionar_DestinoCulinario(marcador):
    if marcador.image_hidden is True:
        marcador.hide_image(False)
    else:
        marcador.hide_image(True)
    #print("Ubicación seleccionada: ", marcador.text)