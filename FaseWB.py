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
        self.escrituraDelNuevoValorPC()
        self.escribirEnBancoDeRegistros()
        return self.comprobarUltimaInstruccion()



    def escribirEnBancoDeRegistros(self):
        if (len(self.registrosAcumulados["FaseMEM"]) >= 2):
            registrosAnteriores = self.registrosAcumulados["FaseMEM"]
            instruccion = registrosAnteriores[0]
            if (instruccion != None):
                if (instruccion.esTipoR()):
                    # guardo registro de acoplamiento entre MEM/WB
                    rd = instruccion.getRd()
                    contenido = registrosAnteriores[1]
                    self.memoriaRegistrosDeAcoplamiento.agregarContenidoEnRegistroAcoplamiento(rd, contenido,
                                                                                               "FaseMEMWB")
                    self.bancoDeRegistros.agregarRegistro(contenido, rd)
                    self.registrosAcumulados["FaseWB"].append(rd)
                elif (instruccion.esLw()):
                    rt = instruccion.getRt()
                    contenido = registrosAnteriores[1]
                    self.memoriaRegistrosDeAcoplamiento.agregarContenidoEnRegistroAcoplamiento(rt, contenido,"FaseMEMWB")
                    self.bancoDeRegistros.agregarRegistro(contenido, rt)
                    self.registrosAcumulados["FaseWB"].append(rt)

    def introducirBurbuja(self):
        registros = self.registrosAcumulados["FaseWB"]
        registros.append(-1)

    def escrituraDelNuevoValorPC(self):
        registros = self.registrosAcumulados["FaseWB"]
        instruccionFaseIF= self.getInstruccionEnFaseIF()
        if(instruccionFaseIF != None):
            if(instruccionFaseIF.esBeq()):
                self.introducirBurbuja() #Primera Burbuja
            elif(instruccionFaseIF.esTipoJ()):
                self.introducirBurbuja()
            elif(instruccionFaseIF.esLw()):
                self.introducirBurbuja()
            else: #de manera normal
                registros.append(self.registrosAcumulados["FaseIF"][1])
        instruccionEnFaseID=self.getInstruccionEnFaseID()
        if(instruccionEnFaseID != None):
            if(instruccionEnFaseID.esBeq()):
                self.introducirBurbuja() #Segunda burbuja
            elif(instruccionEnFaseID.esTipoJ()):
                #escribir pcsalto
                pcSalto=self.registrosAcumulados["FaseID"][1]
                registros.append(pcSalto)
            elif(instruccionEnFaseID.esLw()):
                pcSiguienteInstruccion=self.registrosAcumulados["FaseIF"][2]
                registros.append(pcSiguienteInstruccion)
        if(len(self.registrosAcumulados["FaseEX"]) == 6):
            self.escribirSaltoBeq()
        else:
            if(len(self.registrosAcumulados["FaseIF"] )!= 0):
                registros.append(self.registrosAcumulados["FaseIF"][1])#normal otra vez, por quee ?

    def getInstruccionEnFaseID(self):
        if(len(self.registrosAcumulados["FaseID"]) != 0):
            instruccionID=self.registrosAcumulados["FaseID"][0]
            return instruccionID
    def getInstruccionEnFaseIF(self):
        if (len(self.registrosAcumulados["FaseIF"]) != 0):
            instruccionAnterior = self.registrosAcumulados["FaseIF"][0]
            return instruccionAnterior
    def escribirSaltoBeq(self):
        # La instruccion anterior a none era una instruccion beq
        registros=self.registrosAcumulados["FaseWB"]
        if(self.registrosAcumulados["FaseEX"][3]==0): #es decir que si se produce el salto
            registros = self.registrosAcumulados["FaseWB"]
            registros.append(self.registrosAcumulados["FaseEX"][4])
        else:
            registros.append(self.registrosAcumulados["FaseEX"][5])

    def comprobarUltimaInstruccion(self):
        if(len(self.registrosAcumulados["FaseMEM"])!= 0):
            if(self.registrosAcumulados["FaseID"][0]==None and self.registrosAcumulados["FaseEX"][0] == None
            and self.registrosAcumulados["FaseIF"][0]==None and self.registrosAcumulados["FaseMEM"][0]==None):
                return True
        return False
