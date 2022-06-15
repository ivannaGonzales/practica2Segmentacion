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
            print("---------------FASE MEM---------------")
            registrosFaseEX=self.registrosAcumulados.get("FaseEX")
            instruccion=registrosFaseEX[0]
            if(instruccion!=None):
                print("Instruccion de tipo ", instruccion.getTipo())
            else:
                print("Instruccion vacia")
            regSiguiente = self.registrosAcumulados["FaseMEM"]
            regSiguiente.append(instruccion)
            if(instruccion!=None and not instruccion.esTipoJ()):
                if(instruccion.esLw()):
                    direccionMem = registrosFaseEX[2]
                    contenido=self.memoria.getContenido(direccionMem)
                    print("El valor de la lectura de memoria con la direccion", direccionMem, "es ",contenido)
                    regSiguiente.append(contenido)
                elif(instruccion.esSw()):
                    rt=registrosFaseEX[2]
                    direccionMem = registrosFaseEX[3]
                    print("Se escribio en memoria con la direccion", direccionMem, "el valor", rt)
                    self.memoria.escribirEnMemoria(rt,direccionMem)
                elif(instruccion.esTipoR()):
                    registroEXMEM=registrosFaseEX[3]
                    self.memoriaRegistrosDeAcoplamiento.agregarContenidoEnRegistroAcoplamiento\
                        (instruccion.getRd(),registroEXMEM,"FaseEXMEM")
                    resultado=registrosFaseEX[3]
                    print("El resultado de la ALU", resultado, " es pasado a la faseWB")
                    regSiguiente.append(resultado)
            print(regSiguiente)
