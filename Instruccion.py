class Instruccion():
    def __init__(self,tipo,rs,rt):
        self.tipo=tipo
        self.rs=rs
        self.rt=rt

    def getTipo(self):
        return self.tipo
    def getRs(self):

    def getRt(self):
        return self.rt
    def esLw(self):
        return self.tipo=="lw"
    def esTipoR(self):
        return self.tipo=="add" or self.tipo=="sub"
    def esSw(self):
        return self.tipo=="sw"
    def esBeq(self):
        return self.tipo=="beq"
    def esSub(self):
        return self.tipo=="sub"
    def esAdd(self):
        return self.tipo=="add"
    def esTipoJ(self):
        return self.tipo=="j"
