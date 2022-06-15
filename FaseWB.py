#voy a agregar a todos el pc
from Fase import Fase


class FaseWB(Fase):
    def __init__(self, bancoDeRegistros, registrosAcumulados, parar, memoriaRegistrosDeAcoplamiento):
        self.bancoDeRegistros=bancoDeRegistros
        Fase.__init__(self,registrosAcumulados)
        self.parar=parar
        self.memoriaRegistrosDeAcoplamiento=memoriaRegistrosDeAcoplamiento
    def iniciar(self):
        self.borrarFase("FaseWB")
        if(len(self.registrosAcumulados["FaseWB"])!=0):
            self.memoriaRegistrosDeAcoplamiento.borrarRegistroDeAcoplamiento("FaseMEMWB")
        print("---------------FASE WB---------------")

        self.escrituraDelNuevoValorPC()
        self.escribirEnBancoDeRegistros()

        return self.comprobarUltimaInstruccion()

    def escribirEnBancoDeRegistros(self):
        if (len(self.registrosAcumulados["FaseMEM"]) >= 2):
            registrosAnteriores = self.registrosAcumulados["FaseMEM"]
            instruccion = registrosAnteriores[0]
            if (instruccion !=None):
                if (instruccion.esTipoR()):
                    # guardo registro de acoplamiento entre MEM/WB
                    rd = instruccion.getRd()
                    contenido = registrosAnteriores[1]
                    self.memoriaRegistrosDeAcoplamiento.\
                        agregarContenidoEnRegistroAcoplamiento(rd, contenido,"FaseMEMWB")
                    self.bancoDeRegistros.agregarClaveValor(rd,contenido)
                    self.registrosAcumulados["FaseWB"].append(rd)
                    print("Se ha escrito en el banco de registro, el registro", rd, "con valor", contenido)
                elif (instruccion.esLw()):
                    rt = instruccion.getRt()
                    contenido = registrosAnteriores[1]
                    self.memoriaRegistrosDeAcoplamiento.agregarContenidoEnRegistroAcoplamiento(rt, contenido,"FaseMEMWB")
                    self.bancoDeRegistros.agregarClaveValor(rt,contenido)
                    self.registrosAcumulados["FaseWB"].append(rt)
                    print("Se ha escrito en el banco de registro, el registro", rt, "con valor", contenido)

            print(self.registrosAcumulados["FaseWB"])

    def introducirBurbuja(self):
        registros = self.registrosAcumulados["FaseWB"]
        registros.append(-1)

    def escrituraDelNuevoValorPC(self):
        registros = self.registrosAcumulados["FaseWB"]
        instruccionFaseIF= self.getInstruccionEnFaseIF()
        instruccionEnFaseID = self.getInstruccionEnFaseID()
        if(instruccionFaseIF != None):
            #Primera burbuja
            if(instruccionFaseIF.esBeq()):
                print("Se introdujo la primera burbuja por instruccion beq")
                self.introducirBurbuja()
            elif(instruccionFaseIF.esTipoJ()):
                print("Se introdujo la primera burbuja por instruccion de tipo J")
                self.introducirBurbuja()
            elif(instruccionFaseIF.esLw()):
                print("Se introdujo la primera burbuja por instruccion lw")
                self.introducirBurbuja()
            else: #de manera normal
                print("Pc de la siguiente instruccion", self.registrosAcumulados["FaseIF"][1])
                registros.append(self.registrosAcumulados["FaseIF"][1])

        elif(instruccionEnFaseID != None):
            if(instruccionEnFaseID.esBeq()):
                self.introducirBurbuja() #Segunda burbuja
                print("Se introdujo la segunda burbuja por instruccion beq")
            elif(instruccionEnFaseID.esTipoJ()):
                pcSalto=self.registrosAcumulados["FaseID"][1]
                print("La siguiente instruccion es una instruccion con el pc de salto de la instruccion J", pcSalto)
                registros.append(pcSalto)
            elif(instruccionEnFaseID.esLw()):
                pcSiguienteInstruccion=self.registrosAcumulados["FaseIF"][1]
                print("La siguiente instruccion será la instruccion que se hubiera ejecutado si no se hubiera introducido la burbuja por la instruccion lw", pcSiguienteInstruccion)
                registros.append(pcSiguienteInstruccion)
            else:
                print("Pc de la siguiente instruccion", self.registrosAcumulados["FaseIF"][1])
                registros.append(self.registrosAcumulados["FaseIF"][1])
            #Escribir el salto despues de la segunda burbuja
        elif(len(self.registrosAcumulados["FaseEX"]) == 6):
            self.escribirSaltoBeq()
        else:
            if(len(self.registrosAcumulados["FaseIF"] )!= 0):
                registros.append(self.registrosAcumulados["FaseIF"][1])

    def getInstruccionEnFaseID(self):
        if(len(self.registrosAcumulados["FaseID"]) != 0):
            instruccionID=self.registrosAcumulados["FaseID"][0]
            return instruccionID
    def getInstruccionEnFaseIF(self):
        if (len(self.registrosAcumulados["FaseIF"]) != 0):
            instruccionAnterior = self.registrosAcumulados["FaseIF"][0]
            return instruccionAnterior
    def escribirSaltoBeq(self):
        registros=self.registrosAcumulados["FaseWB"]
        if(self.registrosAcumulados["FaseEX"][3]==0): #es decir que si se produce el salto
            registros = self.registrosAcumulados["FaseWB"]
            print("La siguiente instruccion sera la instruccion de salto de la instruccion beq, con pc ", self.registrosAcumulados["FaseEX"][4])
            registros.append(self.registrosAcumulados["FaseEX"][4]) #salto
        else:
            print("La siguiente instruccion sera la intruccion siguiente de la instruccion beq porque el salto no fue efectivo, con pc", self.registrosAcumulados["FaseEX"][5])
            registros.append(self.registrosAcumulados["FaseEX"][5])#no salto

    def comprobarUltimaInstruccion(self):
        if(len(self.registrosAcumulados["FaseMEM"])!= 0):
            if(self.registrosAcumulados["FaseID"][0]==None and self.registrosAcumulados["FaseEX"][0] == None
            and self.registrosAcumulados["FaseIF"][0]==None and self.registrosAcumulados["FaseMEM"][0]==None):
                return True
            print("Se acabo la ejecucion")
        return False
