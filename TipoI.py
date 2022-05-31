from Instruccion import Instruccion
class TipoI(Instruccion):
    def __init__(self,tipo,rs,rt,offset):
        Instruccion.__init__(self,tipo)
        self.rs=rs
        self.rt=rt
        self.offset=offset
    def getOffset(self):
        return self.offset
    def getRs(self):
        return self.rs
    def getRt(self):
        return self.rt

