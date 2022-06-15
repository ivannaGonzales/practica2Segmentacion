class Fase():
    def __init__(self,registrosAcumulados):
        self.registrosAcumulados=registrosAcumulados

    def getRegistrosAcumulados(self):
        return self.registrosAcumulados
    def borrarFase(self,fase):
        if(len(self.registrosAcumulados[fase])!=0):
            self.registrosAcumulados[fase]=[]