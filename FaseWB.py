#voy a agregar a todos el pc
class FaseWB():
    def __init__(self, bancoDeRegistros, registrosAcumulados, parar, memoriaDeInstrucciones, memoriaRegistrosDeAcoplamiento):
        self.bancoDeRegistros=bancoDeRegistros
        self.registrosAcumulados=registrosAcumulados
        self.parar=parar
        self.memoriaDeInstrucciones=memoriaDeInstrucciones
        self.memoriaRegistrosDeAcoplamiento=memoriaRegistrosDeAcoplamiento
    def iniciar(self):
        if(len(self.registrosAcumulados["FaseWB"])!=0):
            self.memoriaRegistrosDeAcoplamiento.borrarRegistroDeAcoplamiento("FaseMEMWB")
            self.registrosAcumulados["FaseWB"]=[]
        if(len(self.registrosAcumulados["FaseIF"])!=0):
            registros=self.registrosAcumulados["FaseWB"]
            instruccionAnterior=self.registrosAcumulados["FaseIF"][0]
            if(instruccionAnterior!=None):
                if(instruccionAnterior.esTipoJ()):
                    registros.append(-1)#significa que tenego que introducir un None
                elif(instruccionAnterior.esBeq()):
                    registros.append(-1)
                else:
                    registros.append(self.registrosAcumulados["FaseIF"][1])#Aqui seria lo normal
            else:
                #La instruccion anterior a none era una instruccion beq
                if (len(self.registrosAcumulados["FaseEX"]) == 5):
                    registros = self.registrosAcumulados["FaseWB"]
                    registros.append(self.registrosAcumulados["FaseEX"][4])
                elif(len(self.registrosAcumulados["FaseID"])!=0):
                    instruccionID=self.registrosAcumulados["FaseID"][0]
                    if(instruccionID!=None):
                        if(instruccionID.esTipoJ()):
                            # La instruccion anterior a none era una instruccion j
                            calculoDeDireccionDeSalto=self.registrosAcumulados["FaseID"][1]
                            registros = self.registrosAcumulados["FaseWB"]
                            registros.append(calculoDeDireccionDeSalto)
                        elif(instruccionID.esBeq()):
                            registros.append(-1)
                    else:
                        #Tambien es none
                        registros.append(-2)

                #aqui seria si una instruccion es none, solo none sin incrementar
        if(len(self.registrosAcumulados["FaseMEM"])>=2):
            registrosAnteriores=self.registrosAcumulados["FaseMEM"]
            instruccion=registrosAnteriores[0]
            if(instruccion!=None):
                if(instruccion.esTipoR()):
                    #guardo registro de acoplamiento entre MEM/WB
                    rd=instruccion.getRd()
                    contenido=registrosAnteriores[1]
                    self.memoriaRegistrosDeAcoplamiento.agregarContenidoEnRegistroAcoplamiento(rd,contenido,"FaseMEMWB")
                    self.bancoDeRegistros.agregarRegistro(contenido,rd)
                    self.registrosAcumulados["FaseWB"].append(rd)
                elif(instruccion.esLw()):
                    rt=instruccion.getRt()
                    contenido=registrosAnteriores[1]
                    self.memoriaRegistrosDeAcoplamiento.agregarContenidoEnRegistroAcoplamiento(rt, contenido,"FaseMEMWB")
                    self.bancoDeRegistros.agregarRegistro(contenido,rt)
        elif(len(self.registrosAcumulados["FaseMEM"])!=0):
            h = self.memoriaDeInstrucciones
            instruccion=self.registrosAcumulados["FaseMEM"][0]
            p=self.registrosAcumulados["FaseIF"][1]
            g=len(self.memoriaDeInstrucciones)
            if(self.registrosAcumulados["FaseIF"][1]==len(self.memoriaDeInstrucciones) and instruccion==None):
                    self.parar=True
                    self.registrosAcumulados["FaseWB"].append(self.parar)
                    return self.parar
