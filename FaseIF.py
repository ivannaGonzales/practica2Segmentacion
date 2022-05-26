#Devuelve el pc y la instruccion leida
class FaseIF():
    def __init__(self,pc,memoriaInstrucciones,registrosAcumulados):
        self.pc=pc
        self.memoriaInstrucciones=memoriaInstrucciones
        self.registrosAcumulados=registrosAcumulados#devuelve rs y rt

    def getInstruccionLeida(self):
        if(len(self.registrosAcumulados["FaseWB"])!=0):
            nuevoPc=self.registrosAcumulados["FaseWB"][0]
            if(nuevoPc==-1):
                #aqui tengo que introducir un None
                return None
        #self.pc=nuevoPc
        else:
            if(self.pc>=len(self.memoriaInstrucciones.getMemoriaDeInstrucciones())):
                return None
            else:
                return self.memoriaInstrucciones.getInstruccion(self.pc)
    def incrementarPC(self):
        self.pc=self.pc+1
        return self.pc
    def iniciar(self):
        #Aqui tambien se ha ido agrupando, tu la misma
        #cojo la etapa anterior
        instruccionActual = self.getInstruccionLeida()
        if(instruccionActual!=None):
            pcIncrementado = self.incrementarPC()
        else:
            pcIncrementado=self.pc+1
        if(len(self.registrosAcumulados["FaseIF"])!=0):
            #borro la instruccion anterior
            self.registrosAcumulados["FaseIF"] = []
        registros=self.registrosAcumulados["FaseIF"]
        registros.append(instruccionActual)
        registros.append(pcIncrementado)
        return registros
