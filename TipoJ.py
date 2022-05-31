from Instruccion import Instruccion

class TipoJ(Instruccion):
    def __init__(self,tipo,etiqueta):
        Instruccion.__init__(self, tipo)
        self.etiqueta=etiqueta
    def getEtiqueta(self):
        return self.etiqueta
    def esTipoJ(self):
        return self.tipo=="j"