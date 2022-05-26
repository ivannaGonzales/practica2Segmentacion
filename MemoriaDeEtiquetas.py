class MemoriaDeEtiquetas():
    def __init__(self,memoriaDeEtiquetas):
        self.memoriaDeEtiquetas=memoriaDeEtiquetas

    def iniciarMemoriaDeEtiquetas(self):
        f=open('etiquetas.txt','r')
        for linea in f:
            linea=linea.rstrip()
            self.agregarEtiquetasDesdeLinea(linea)
    def agregarEtiquetasDesdeLinea(self,linea):
        etiquetaynumInstruccion=linea.split(" ")
        etiqueta=etiquetaynumInstruccion[0]
        numInstruccion=etiquetaynumInstruccion[1]
        self.agregarEtiqueta(etiqueta,numInstruccion)
    def agregarEtiqueta(self,etiqueta,numInstruccion):
        self.memoriaDeEtiquetas[etiqueta]=int(numInstruccion)
    def getNumInstruccion(self,etiqueta):
        return self.memoriaDeEtiquetas[etiqueta]