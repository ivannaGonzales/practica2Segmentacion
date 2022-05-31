#Devuelve el pc y la instruccion leida
class FaseIF():
    def __init__(self,pc,memoriaInstrucciones,registrosAcumulados):
        self.pc=pc
        self.memoriaInstrucciones=memoriaInstrucciones
        self.registrosAcumulados=registrosAcumulados#devuelve rs y rt

    def getInstruccionLeida(self):
        if(len(self.registrosAcumulados["FaseWB"])!=0):
            nuevoPc=self.registrosAcumulados["FaseWB"][0]
            self.pc=nuevoPc
            if(nuevoPc==-1):
                return None
            else:
                if(self.pc>=len(self.memoriaInstrucciones.getMemoriaDeInstrucciones())):
                    self.pc=nuevoPc
                    return None
                else:
                    return self.memoriaInstrucciones.getInstruccion(self.pc)
        else:
            return self.memoriaInstrucciones.getInstruccion(self.pc) #Esta seria la primera instruccion, leo la primera instruccion
    def incrementarPC(self):
        self.pc=self.pc+1
        return self.pc
    def iniciar(self):
        #solo me da la instruccion
        instruccionActual = self.getInstruccionLeida()
        #quiero comprobar que la instruccion actual es lw y la anterior es un None
        if(len(self.registrosAcumulados["FaseIF"])!=0):
            pcInstruccionAnterior=self.registrosAcumulados["FaseIF"][1]
        if(len(self.registrosAcumulados["FaseIF"])!=0):
            #borro la instruccion anterior
            self.registrosAcumulados["FaseIF"] = []
        if(self.pc == len(self.memoriaInstrucciones.getMemoriaDeInstrucciones())):
            pcIncrementado = self.pc
        else:
            pcIncrementado=self.pc + 1
        registros=self.registrosAcumulados["FaseIF"]
        registros.append(instruccionActual)
        registros.append(pcIncrementado)
        #si la instruccion es beq
        if(instruccionActual != None):
            if(instruccionActual.esBeq()):
                registros.append(pcIncrementado)
        else:
            registros.append(pcIncrementado + 1)

        return registros
