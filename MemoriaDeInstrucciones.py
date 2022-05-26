class MemoriaDeInstrucciones():
    def __init__(self,memoriaDeInstrucciones):
        self.memoriaDeInstrucciones=memoriaDeInstrucciones

    def getMemoriaDeInstrucciones(self):
        return self.memoriaDeInstrucciones
    def agregarInstruccion(self,posInstruccion,instruccion):
        self.memoriaDeInstrucciones[posInstruccion]=instruccion
    def getInstruccion(self,pos):
        return self.memoriaDeInstrucciones[pos]


