#Calculo de la direccion de memoria, el calculo se realiza a traves de la UAL
#Calculo de la direccion de memoria, el calculo se realiza a traves de la UAL
from ALU import ALU
from Fase import Fase
from TipoR import TipoR
from TipoI import TipoI
class FaseEX(Fase):
    def __init__(self,registrosAcumulados,alu,memoriaRegistrosFinalesyAcoplamiento):
        self.alu=alu
        Fase.__init__(self,registrosAcumulados)
        self.memoriaRegistrosFinalesyAcoplamiento=memoriaRegistrosFinalesyAcoplamiento

    def iniciar(self):
        if(len(self.registrosAcumulados["FaseID"])!=0):
            registrosAnteriores=self.registrosAcumulados["FaseID"]
            instruccion=registrosAnteriores[0]
            self.borrarFase("FaseEX")
            regSiguiente = self.registrosAcumulados["FaseEX"]
            regSiguiente.append(instruccion)
            if(instruccion!=None):
                if(instruccion.esLw()):
                    offset=instruccion.getOffset()
                    rsID=registrosAnteriores[1]
                    rs = self.comprobarRegistroAcoplamiento(instruccion.getRs(), rsID)
                    direccionMemoria=self.alu.getResultado(offset,rs,"suma")
                    regSiguiente.append(rs)
                    regSiguiente.append(direccionMemoria)
                elif(instruccion.esSw()):
                    offset=instruccion.getOffset()
                    rsID=registrosAnteriores[1]
                    rtID=registrosAnteriores[2]
                    rs = self.comprobarRegistroAcoplamiento(instruccion.getRs(), rsID)
                    rt = self.comprobarRegistroAcoplamiento(instruccion.getRt(), rtID)
                    direccionMemoria = self.alu.getResultado(offset, rs, "suma")
                    regSiguiente.append(rs)
                    regSiguiente.append(rt)
                    regSiguiente.append(direccionMemoria)
                elif(instruccion.esTipoR()):
                    rsID=registrosAnteriores[1]
                    rtID=registrosAnteriores[2]

                    # Puede usar de entrada de la ALU tanto como los registros de acoplamiento de EXMEM y de MEMWB

                    rs=self.comprobarRegistroAcoplamiento(instruccion.getRs(),rsID)
                    rt=self.comprobarRegistroAcoplamiento(instruccion.getRt(),rtID)


                    if(instruccion.esAdd()):
                        resultado=self.alu.getResultado(rs,rt,"suma")
                    elif(instruccion.esSub()):
                        resultado=self.alu.getResultado(rs,rt,"resta")
                    else:
                        resultado=self.alu.getResultado(rs,rt,"multiplicacion")

                    regSiguiente.append(rs)
                    regSiguiente.append(rt)
                    regSiguiente.append(resultado)
                elif(instruccion.esBeq()):
                    rsID = registrosAnteriores[1] #valor numerico
                    rtID = registrosAnteriores[2]
                    rs=self.comprobarRegistroAcoplamiento(instruccion.getRs(),rsID)
                    rt=self.comprobarRegistroAcoplamiento(instruccion.getRt(),rtID)
                    resultado = self.alu.getResultado(rs, rt, "resta")
                    pcRamificacion=registrosAnteriores[3]
                    regSiguiente.append(rs)
                    regSiguiente.append(rt)
                    regSiguiente.append(resultado)
                    regSiguiente.append(pcRamificacion)
                    pcIncrementado=registrosAnteriores[4]
                    regSiguiente.append(pcIncrementado)



    def comprobarRegistroAcoplamiento(self,registro,registroNumerico):
        nuevoRegistro=registroNumerico
        if (self.memoriaRegistrosFinalesyAcoplamiento.esRegistroFinal(registro)):
            if (self.memoriaRegistrosFinalesyAcoplamiento.esRegistroDeAcoplamiento(registro)):
                nuevoRegistro= self.memoriaRegistrosFinalesyAcoplamiento.getContenidoDeRegistroDeAcoplamiento(
                    registro)
        return nuevoRegistro




