class BancoDeRegistros():
    def __init__(self,bancoDeRegistros):
        self.bancoDeRegistros=bancoDeRegistros

    def getBancoDeRegistros(self):
        return self.bancoDeRegistros
    def agregarRegistro(self,contenido,registro):
        self.bancoDeRegistros[registro]=int(contenido)
    def iniciarbancoDeRegistros(self):
        f = open('bancoDeRegistro.txt', 'r')
        for linea in f:
            linea=linea.rstrip()
            self.agregarRegistroDesdeLinea(self.bancoDeRegistros,linea)

    def agregarRegistroDesdeLinea(self,bancoDeRegistros,linea):
        instruccion=linea.split(" ")
        registroycontenido=instruccion[1]
        registroycontenido=registroycontenido.split(",")
        registro=registroycontenido[0]
        contenido=registroycontenido[1]
        self.agregarRegistro(contenido,registro)

    def getContenido(self,registro):
        return self.bancoDeRegistros[registro]



