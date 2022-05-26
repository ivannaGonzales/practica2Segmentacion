from Instruccion import Instruccion
class TipoR(Instruccion):
    def __init__(self,tipo,rs,rt,rd):
        Instruccion.__init__(self,tipo,rs,rt)
        self.rd=rd

    def getRd(self):
        return self.rd
    def getOperacion(self):
        if(self.tipo=="add"):
            op="suma"
        elif(self.tipo=="sub"):
            op="resta"
        return op


