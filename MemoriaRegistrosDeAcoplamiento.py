class MemoriaRegistrosDeAcoplamiento():
    def __init__(self,memoriaRegistrosFinal,registrosDeAcoplamiento,registrosDeAcoplamientoyContenido
                 ,registroDeAcoplamientoPorFase):
        self.memoriaRegistrosFinal=memoriaRegistrosFinal
        self.registrosDeAcoplamiento=registrosDeAcoplamiento
        self.registrosDeAcoplamientoyContenido=registrosDeAcoplamientoyContenido
        self.registroDeAcoplamientoPorFase=registroDeAcoplamientoPorFase

    def esRegistroDeAcoplamiento(self,registro):
        return registro in self.registrosDeAcoplamiento
    #Esto esta bien
    def esRegistroFinal(self,registro):
        return registro in self.memoriaRegistrosFinal
    def agregarContenidoEnRegistroAcoplamiento(self,registro,contenido,fase):
        self.registrosDeAcoplamientoyContenido[registro]=contenido
        self.registroDeAcoplamientoPorFase[fase]=registro
        self.registrosDeAcoplamiento.append(registro)
    def getContenidoDeRegistroDeAcoplamiento(self,registro):
        return self.registrosDeAcoplamientoyContenido[registro]
    def borrarRegistroDeAcoplamiento(self,fase):
        registroDeAcoplamiento=self.registroDeAcoplamientoPorFase.get(fase)
        if(registroDeAcoplamiento!=None):
            self.registrosDeAcoplamiento.remove(registroDeAcoplamiento)
            self.registroDeAcoplamientoPorFase.pop(fase)
            if (not registroDeAcoplamiento in self.registrosDeAcoplamiento):  # osea si todavia esta no se borra
                self.registrosDeAcoplamientoyContenido.pop(registroDeAcoplamiento)
    def agregarRegistroFinal(self,registro):
        self.memoriaRegistrosFinal.append(registro)
