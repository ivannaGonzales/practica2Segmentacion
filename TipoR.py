from Instruccion import Instruccion
class TipoR(Instruccion):
    def __init__(self,tipo,rs,rt,rd):
        Instruccion.__init__(self,tipo)
        self.rs=rs
        self.rd=rd
        self.rt=rt

    def getRd(self):
        return self.rd
    def getRs(self):
        return self.rs
    def getRt(self):
        return self.rt
    def getOperacion(self):
        if(self.tipo=="add"):
            op="suma"
        elif(self.tipo=="sub"):
            op="resta"
        else:
            op="multiplicacion"
        return op


