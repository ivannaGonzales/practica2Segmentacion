#Calculo de la direccion de memoria, el calculo se realiza a traves de la UAL
from ALU import ALU
from TipoR import TipoR
from TipoI import TipoI
class FaseEX():
    def __init__(self,registrosAcumulados,alu,memoriaRegistrosFinalesyAcoplamiento,memoriaInstrucciones):
        self.alu=alu
        self.registrosAcumulados=registrosAcumulados
        self.memoriaRegistrosFinalesyAcoplamiento=memoriaRegistrosFinalesyAcoplamiento
        self.memoriaInstrucciones=memoriaInstrucciones

    def iniciar(self):
        if(len(self.registrosAcumulados["FaseID"])!=0):
            registrosAnteriores=self.registrosAcumulados["FaseID"]
            instruccion=registrosAnteriores[0]
            if(len(self.registrosAcumulados["FaseEX"])!=0):
                self.registrosAcumulados["FaseEX"]=[]
            regSiguiente = self.registrosAcumulados["FaseEX"]
            regSiguiente.append(instruccion)
            if(instruccion!=None):
                if(instruccion.esTipoJ()):
                    pass
                elif(instruccion.esLw()):
                    offset=instruccion.getOffset()
                    rs=registrosAnteriores[1]
                    direccionMemoria=self.alu.getResultado(offset,rs,"suma")
                    if (not self.memoriaInstrucciones.getInstruccion(0) == instruccion):  # que no sea la primera instruccion
                        # Puede usar de entrada de la ALU tanto como los registros de acoplamiento de EXMEM y de MEMWB
                        if (self.memoriaRegistrosFinalesyAcoplamiento.esRegistroFinal(instruccion.getRs())):
                            if (self.memoriaRegistrosFinalesyAcoplamiento.esRegistroDeAcoplamiento):
                                rs=self.memoriaRegistrosFinalesyAcoplamiento.getContenidoDeRegistroDeAcoplamiento(instruccion.getRs())
                    regSiguiente.append(rs)
                    regSiguiente.append(direccionMemoria)
                elif(instruccion.esSw()):
                    offset=instruccion.getOffset()
                    rs=registrosAnteriores[1]
                    rt=registrosAnteriores[2]
                    direccionMemoria = self.alu.getResultado(offset, rs, "suma")
                    regSiguiente.append(rs)
                    regSiguiente.append(rt)
                    regSiguiente.append(direccionMemoria)
                elif(instruccion.esTipoR()):
                    rs=registrosAnteriores[1]
                    rt=registrosAnteriores[2]
                    if(not self.memoriaInstrucciones.getInstruccion(0)==instruccion):#que no sea la primera instruccion
                        #Puede usar de entrada de la ALU tanto como los registros de acoplamiento de EXMEM y de MEMWB
                        #AHORA VOY A PREGUNTAR SI LA INSTRUCCION ES ANTERIOR ES LW, PORQUE CREO BURBUJA Y BORRO
                        q=instruccion.getRs()
                        hi=instruccion.getRs()
                        if(self.memoriaRegistrosFinalesyAcoplamiento.esRegistroFinal(instruccion.getRs())):
                            if(len(self.registrosAcumulados["FaseMEM"])!=0):
                                instruccionAnterior = self.registrosAcumulados["FaseMEM"][0]
                                if(instruccionAnterior != None):
                                    if(instruccionAnterior.esLw()):
                                        if(instruccionAnterior.getRt()==instruccion.getRs()):
                                            #necesito borrar la instruccion actual y colocar un None
                                            self.borrarInstruccion(instruccion)
                            if(self.memoriaRegistrosFinalesyAcoplamiento.esRegistroDeAcoplamiento(instruccion.getRs())):
                                rs=self.memoriaRegistrosFinalesyAcoplamiento.getContenidoDeRegistroDeAcoplamiento(instruccion.getRs())
                        elif(self.memoriaRegistrosFinalesyAcoplamiento.esRegistroFinal(instruccion.getRt())):
                            if(self.memoriaRegistrosFinalesyAcoplamiento.esRegistroDeAcoplamiento(instruccion.getRt())):
                                rt=self.memoriaRegistrosFinalesyAcoplamiento.getContenidoDeRegistroDeAcoplamiento(instruccion.getRt())
                    if(instruccion.esAdd()):
                        resultado=self.alu.getResultado(rs,rt,"suma")
                    elif(instruccion.esSub()):
                        resultado=self.alu.getResultado(rs,rt,"resta")
                    regSiguiente.append(rs)
                    regSiguiente.append(rt)
                    regSiguiente.append(resultado)
                elif(instruccion.esBeq()):
                    rs = registrosAnteriores[1]
                    rt = registrosAnteriores[2]
                    if (not self.memoriaInstrucciones.getInstruccion(0) == instruccion):  # que no sea la primera instruccion
                        # Puede usar de entrada de la ALU tanto como los registros de acoplamiento de EXMEM y de MEMWB
                        if (self.memoriaRegistrosFinalesyAcoplamiento.esRegistroFinal(instruccion.getRs())):
                            if (self.memoriaRegistrosFinalesyAcoplamiento.esRegistroDeAcoplamiento(instruccion.getRs())):
                                rs = self.memoriaRegistrosFinalesyAcoplamiento.getContenidoDeRegistroDeAcoplamiento(
                                    instruccion.getRs())
                        if (self.memoriaRegistrosFinalesyAcoplamiento.esRegistroFinal(instruccion.getRt())):
                            if (self.memoriaRegistrosFinalesyAcoplamiento.esRegistroDeAcoplamiento(instruccion.getRt())):
                                rt=self.memoriaRegistrosFinalesyAcoplamiento.getContenidoDeRegistroDeAcoplamiento(
                                    instruccion.getRt())
                    resultado = self.alu.getResultado(rs, rt, "resta")
                    pcRamificacion=registrosAnteriores[3]
                    regSiguiente.append(rs)
                    regSiguiente.append(rt)
                    regSiguiente.append(resultado)
                    regSiguiente.append(pcRamificacion)
                    pcIncrementado=registrosAnteriores[4]
                    regSiguiente.append(pcIncrementado)
    def borrarInstruccion(self,instruccion):
        #Hasta aqui tengo que borrar la fase IF,ID y la EX
        self.registrosAcumulados["FaseEX"]=[]
        self.registrosAcumulados["FaseEX"]=[None]
        self.registrosAcumulados["FaseID"]=[None]
        self.registrosAcumulados["FaseIF"]=[None]





