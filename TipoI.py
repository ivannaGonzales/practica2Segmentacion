from Instruccion import Instruccion
class TipoI(Instruccion):
    def __init__(self,tipo,rs,rt,offset):
        Instruccion.__init__(self,tipo,rs,rt)
        self.offset=offset
    def getOffset(self):
        return self.offset

