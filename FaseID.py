#Decodificacion, lectura de operandos fuente y calculo de direccion de ramificacion
from Fase import Fase


class FaseID(Fase):
    def __init__(self,registrosAcumulados,bancoDeRegistros,etiquetas):
        Fase.__init__(self,registrosAcumulados)
        self.bancoDeRegistros=bancoDeRegistros
        self.etiquetas=etiquetas

    def iniciar(self):
        self.borrarFase("FaseID")
        if(len(self.registrosAcumulados["FaseIF"])!=0):
            registros = self.registrosAcumulados["FaseID"]
            regAnterior=self.registrosAcumulados["FaseIF"]
            instruccion=regAnterior[0]
            registros.append(instruccion)
            if(instruccion!=None):
                if(instruccion.esTipoJ()):
                    self.calculoDeDireccionSalto(registros)
                elif(instruccion.esSw()):
                    rs=self.bancoDeRegistros.getContenido(instruccion.getRs())
                    rt=self.bancoDeRegistros.getContenido(instruccion.getRt())
                    registros.append(rs)
                    registros.append(rt)
                elif(instruccion.esTipoR()):
                    rs=self.bancoDeRegistros.getContenido(instruccion.getRs())
                    rt=self.bancoDeRegistros.getContenido(instruccion.getRt())
                    registros.append(rs)
                    registros.append(rt)
                elif(instruccion.esBeq()):
                    rs = self.bancoDeRegistros.getContenido(instruccion.getRs())
                    rt = self.bancoDeRegistros.getContenido(instruccion.getRt())
                    registros.append(rs)
                    registros.append(rt)
                    self.calculoDeDireccionRamificacion(registros)
                    #voy a agregar lo otro
                    pcIncrementado=regAnterior[1]
                    registros.append(pcIncrementado)
                    #tengo que decirle a la siguiente fase de IF que hay que intoducir una isntruccion nula
                elif(instruccion.esLw()):

                    rs=self.bancoDeRegistros.getContenido(instruccion.getRs())
                    registros.append(rs)

    def calculoDeDireccionRamificacion(self,registros):
        if(len(self.registrosAcumulados["FaseIF"])!=0):
            instruccion=self.registrosAcumulados["FaseIF"][0]
            if(instruccion!=None):
                if(instruccion.esBeq()):
                    etiqueta=instruccion.getEtiqueta()
                    numInstruccion=self.etiquetas.getValor(etiqueta)
                    pcRamificacion=numInstruccion
                    registros.append(pcRamificacion)
    def calculoDeDireccionSalto(self,registros):
        if(len(self.registrosAcumulados["FaseIF"])!=0):
            instruccion=self.registrosAcumulados["FaseIF"][0]
            if(instruccion!=None):
                if(instruccion.esTipoJ()):
                    etiqueta=instruccion.getEtiqueta()
                    numInstruccion = self.etiquetas.getValor(etiqueta)
                    pcSalto = numInstruccion
                    registros.append(pcSalto)
