#Decodificacion, lectura de operandos fuente y calculo de direccion de ramificacion
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
            print("---------------FASE ID---------------")
            registros = self.registrosAcumulados["FaseID"]
            regAnterior=self.registrosAcumulados["FaseIF"]
            instruccion=regAnterior[0]
            if (instruccion != None):
                print("Instruccion de tipo ", instruccion.getTipo())
            else:
                print("Instruccion vacia")
            registros.append(instruccion)
            if(instruccion!=None):
                if(instruccion.esTipoJ()):
                    direccionSalto=self.calculoDeDireccionSalto()
                    registros.append(direccionSalto)
                    print("Se calculo la direccion de salto", direccionSalto)
                elif(instruccion.esSw()):
                    rs=self.bancoDeRegistros.getContenido(instruccion.getRs())
                    rt=self.bancoDeRegistros.getContenido(instruccion.getRt())
                    print("Se obtuvo el registro rs ",rs)
                    print("Se obtuvo el registro rt ",rt)
                    registros.append(rs)
                    registros.append(rt)
                elif(instruccion.esTipoR()):
                    rs=self.bancoDeRegistros.getContenido(instruccion.getRs())
                    rt=self.bancoDeRegistros.getContenido(instruccion.getRt())
                    print("Se obtuvo el registro rs ", rs)
                    print("Se obtuvo el registro rt ", rt)
                    registros.append(rs)
                    registros.append(rt)
                elif(instruccion.esBeq()):
                    rs = self.bancoDeRegistros.getContenido(instruccion.getRs())
                    rt = self.bancoDeRegistros.getContenido(instruccion.getRt())
                    print("Se obtuvo el registro rs ", rs)
                    print("Se obtuvo el registro rt ", rt)
                    registros.append(rs)
                    registros.append(rt)
                    direccionRamificacion=self.calculoDeDireccionRamificacion()
                    registros.append(direccionRamificacion)
                    #pc incrementado de la fase IF
                    pcIncrementado=regAnterior[1]
                    registros.append(pcIncrementado)
                elif(instruccion.esLw()):
                    rs=self.bancoDeRegistros.getContenido(instruccion.getRs())
                    registros.append(rs)
                    print("Se obtuvo el registro rs ", rs)
            print(registros)

    def calculoDeDireccionRamificacion(self):
        if(len(self.registrosAcumulados["FaseIF"])!=0):
            instruccion=self.registrosAcumulados["FaseIF"][0]
            if(instruccion!=None):
                if(instruccion.esBeq()):
                    etiqueta=instruccion.getEtiqueta()
                    numInstruccion=self.etiquetas.getValor(etiqueta)
                    pcRamificacion=numInstruccion
                    return pcRamificacion
    def calculoDeDireccionSalto(self):
        if(len(self.registrosAcumulados["FaseIF"])!=0):
            instruccion=self.registrosAcumulados["FaseIF"][0]
            if(instruccion!=None):
                if(instruccion.esTipoJ()):
                    etiqueta=instruccion.getEtiqueta()
                    numInstruccion = self.etiquetas.getValor(etiqueta)
                    pcSalto = numInstruccion
                    return pcSalto

