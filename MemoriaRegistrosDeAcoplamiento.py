class MemoriaRegistrosDeAcoplamiento():
    def __init__(self,registrosDeAcoplamientoyContenido
                 ,registroDeAcoplamientoPorFase):
        self.registrosDeAcoplamientoyContenido=registrosDeAcoplamientoyContenido
        self.registroDeAcoplamientoPorFase=registroDeAcoplamientoPorFase
    def agregarContenidoEnRegistroAcoplamiento(self,registro,contenido,fase):
        self.registrosDeAcoplamientoyContenido[registro]=contenido
        self.registroDeAcoplamientoPorFase[fase]=registro
    def getContenidoDeRegistroDeAcoplamiento(self,registro):
        return self.registrosDeAcoplamientoyContenido.get(registro)
    def borrarRegistroDeAcoplamiento(self,fase):
        registroDeAcoplamiento=self.registroDeAcoplamientoPorFase.get(fase)
        if(registroDeAcoplamiento!=None):
            self.registroDeAcoplamientoPorFase.pop(fase)
            self.registrosDeAcoplamientoyContenido.pop(registroDeAcoplamiento)

