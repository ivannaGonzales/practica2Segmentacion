class Estructura():
    def __init__(self,memoria):
        self.memoria=memoria
    def getMemoria(self):
        return self.memoria
    def getContenido(self,contenido):
        return self.memoria.get(contenido)
    def escribirEnMemoria(self,clave,valor):
        self.memoria[clave]=valor

    def iniciar(self,ficheroDeTexto,formato):
        f=open(ficheroDeTexto,'r')
        for linea in f:
            linea=linea.rstrip()
            self.agregarContenidoDesdeLinea(linea,formato)
    def agregarContenidoDesdeLinea(self,linea,formato):
        claveyvalor=linea.split(" ")
        clave=claveyvalor[0]
        valor=claveyvalor[1]
        if(formato=="numero"):
            clave=int(clave)
            valor=int(valor)
        else:
            #la clave sera un string
            valor=int(valor)

        self.agregarClaveValor(clave,valor)

    def agregarClaveValor(self,clave,valor):
        self.memoria[clave]=valor
    def getValor(self,clave):
        return self.memoria[clave]
