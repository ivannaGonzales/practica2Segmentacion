from Instruccion import Instruccion
class TipoBeq(Instruccion):
    def __init__(self,tipo,rs,rt,etiqueta):
        Instruccion.__init__(self,tipo,rs,rt)
        self.etiqueta=etiqueta
    def getEtiqueta(self):
        return self.etiqueta
