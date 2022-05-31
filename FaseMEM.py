from Fase import Fase


class FaseMEM(Fase):
    def __init__(self,registrosAcumulados,memoria,memoriaRegistroDeAcoplamiento):
        Fase.__init__(self,registrosAcumulados)
        self.memoria=memoria
        self.memoriaRegistrosDeAcoplamiento=memoriaRegistroDeAcoplamiento


    def iniciar(self):
        if(len(self.registrosAcumulados["FaseEX"])!=0):
            self.borrarFase("FaseMEM")
            if (len(self.registrosAcumulados["FaseMEM"]) != 0):
                self.memoriaRegistrosDeAcoplamiento.borrarRegistroDeAcoplamiento("FaseEXMEM")
            registrosFaseEX=self.registrosAcumulados.get("FaseEX")
            instruccion=registrosFaseEX[0]
            regSiguiente = self.registrosAcumulados["FaseMEM"]
            regSiguiente.append(instruccion)
            if(instruccion!=None and not instruccion.esTipoJ()):
                #aqui guardo el registro de acoplamiento
                if(instruccion.esLw()):
                    direccionMem = registrosFaseEX[2]
                    contenido=self.memoria.getContenido(direccionMem)
                    regSiguiente.append(contenido)
                elif(instruccion.esSw()):
                    rt=registrosFaseEX[2]
                    direccionMem = registrosFaseEX[3]
                    self.memoria.escribirEnMemoria(rt,direccionMem)
                elif(instruccion.esTipoR()):
                    #tengo que borrar el anterior registro de acoplamiento
                    registroEXMEM=registrosFaseEX[3]
                    self.memoriaRegistrosDeAcoplamiento.agregarContenidoEnRegistroAcoplamiento(instruccion.getRd(),registroEXMEM,"FaseEXMEM")
                    resultado=registrosFaseEX[3]
                    #instruccion y resultado
                    regSiguiente.append(resultado)

