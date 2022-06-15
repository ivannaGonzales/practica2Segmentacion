from Instruccion import Instruccion
class TipoBeq(Instruccion):
    def __init__(self,tipo,rs,rt,etiqueta):
        Instruccion.__init__(self,tipo)
        self.etiqueta=etiqueta
        self.rs=rs
        self.rt=rt
    def getEtiqueta(self):
        return self.etiqueta
    def getRs(self):
        return self.rs
    def getRt(self):
        return self.rt

