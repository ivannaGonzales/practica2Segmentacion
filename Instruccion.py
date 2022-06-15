class Instruccion():
    def __init__(self,tipo):
        self.tipo=tipo

    def getTipo(self):
        return self.tipo

    def esLw(self):
        return self.tipo == "lw"
    def esSw(self):
        return self.tipo == "sw"

    def esTipoJ(self):
        return self.tipo == "j"
    def esSub(self):
        return self.tipo=="sub"
    def esAdd(self):
        return self.tipo == "add"
    def esMul(self):
        return self.tipo=="mul"
    def esTipoR(self):
        return self.tipo=="add" or self.tipo=="sub" or self.tipo=="mul"
    def esBeq(self):
        return self.tipo =="beq"
    def esVacia(self):
        return self ==None



