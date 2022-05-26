class TipoJ():
    def __init__(self,tipo,etiqueta):
        self.tipo=tipo
        self.etiqueta=etiqueta
    def getEtiqueta(self):
        return self.etiqueta
    def esTipoJ(self):
        return self.tipo=="j"