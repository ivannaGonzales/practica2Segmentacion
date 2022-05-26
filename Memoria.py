class Memoria():
    def __init__(self,memoria):
        self.memoria=memoria

    def getMemoria(self):
        return self.memoria
    def getContenido(self,direccionDeMemoria):
        return self.memoria[direccionDeMemoria]
    def escribirEnMemoria(self,datoLeido,direccionDeMemoria):
        self.memoria[direccionDeMemoria]=datoLeido
    def iniciar(self):
        f=open('memoria.txt','r')
        for linea in f:
            linea=linea.rstrip()
            self.agregarDireccionDesdeLinea(self.memoria,linea)

    def agregarDireccionDesdeLinea(self,memoria,linea):
        direccionycontenido=linea.split(" ")
        direccion=int(direccionycontenido[0])
        contenido=int(direccionycontenido[1])
        self.memoria[direccion]=contenido