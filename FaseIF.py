#Devuelve el pc y la instruccion leida
from Fase import Fase


class FaseIF(Fase):
    def __init__(self,pc,memoriaInstrucciones,registrosAcumulados):
        self.pc=pc
        self.memoriaInstrucciones=memoriaInstrucciones
        Fase.__init__(self,registrosAcumulados)

    def getInstruccionLeida(self):
        if(len(self.registrosAcumulados["FaseWB"])!=0):
            nuevoPc=self.registrosAcumulados["FaseWB"][0]
            self.pc=nuevoPc
            if(nuevoPc==-1):
                print("Instruccion vacia")
                return None
            else:
                if(self.pc>=len(self.memoriaInstrucciones.getMemoriaDeInstrucciones())):
                    self.pc=nuevoPc
                    print("Instruccion vacia")
                    return None
                else:
                    print("Instruccion de tipo", self.memoriaInstrucciones.getInstruccion(self.pc).getTipo())
                    return self.memoriaInstrucciones.getInstruccion(self.pc)
        else:
            return self.memoriaInstrucciones.getInstruccion(self.pc) #Esta seria la primera instruccion, leo la primera instruccion
    def incrementarPC(self):
        self.pc=self.pc+1
        return self.pc
    def iniciar(self):
        print("---------------FASE IF---------------")
        instruccionActual = self.getInstruccionLeida()

        #instruccion actual es la ultima
        if(self.pc == len(self.memoriaInstrucciones.getMemoriaDeInstrucciones())):
            pcIncrementado = self.pc #no lo aumento
        else:
            if(self.pc==-1):
                #cojo el pcIncrementado de la instruccionAnterior
                if (len(self.registrosAcumulados["FaseIF"]) != 0):
                    pcIncrementado = self.registrosAcumulados["FaseIF"][1]
            else:
                pcIncrementado=self.pc+1 #normal
        self.borrarFase("FaseIF")
        registros=self.registrosAcumulados["FaseIF"]
        registros.append(instruccionActual)
        print("Pc incrementado", pcIncrementado)
        registros.append(pcIncrementado)
        print(registros)
        return registros
    def getPc(self):
        return self.pc
