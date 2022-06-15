from Estructura import Estructura
from MemoriaDeInstrucciones import MemoriaDeInstrucciones
from Instruccion import Instruccion
from TipoI import TipoI
from TipoR import TipoR
from FaseIF import FaseIF
from FaseID import FaseID
from FaseEX import FaseEX
from FaseMEM import FaseMEM
from ALU import ALU
from BancoDeRegistros import BancoDeRegistros
from Memoria import Memoria
from FaseWB import FaseWB
from TipoBeq import TipoBeq
from TipoJ import TipoJ
from MemoriaDeEtiquetas import MemoriaDeEtiquetas
from MemoriaRegistrosDeAcoplamiento import MemoriaRegistrosDeAcoplamiento
def crearInstruccion(linea,memoriaRegistrosDeAcoplamientoyFinales):
    contenidoInstruccion=linea.split(" ")
    tipo=contenidoInstruccion[0]
    if(tipo=="j"):
        etiqueta=contenidoInstruccion[1]
        instruccion=TipoJ(tipo,etiqueta)
    registros=contenidoInstruccion[1]
    registros=registros.split(",")
    if(tipo=="add" or tipo=="sub" or tipo=="mul"):
        rd=registros[0]
        rs=registros[1]
        rt=registros[2]
        instruccion=TipoR(tipo,rs,rt,rd)
    elif(tipo=="sw"or tipo=="lw"):
        rt=registros[0]
        offsetyrs=registros[1]
        offsetyrs=offsetyrs.split("(")
        offset=offsetyrs[0]
        rs=offsetyrs[1]
        rs=rs[0:len(rs)-1]
        instruccion=TipoI(tipo,rs,rt,offset)
    elif(tipo=="beq"):#Es de tipo salto
        rs=registros[0]
        rt=registros[1]
        offset=registros[2]
        instruccion=TipoBeq(tipo,rs,rt,offset)
    return instruccion


def inicio(memoriaInstrucciones, bancoDeRegistros, alu, memoria, pc, etiquetas,memoriaRegistrosDeAcoplamiento):
    i = 0
    registrosAcumulados = {}  # se va acumulando todos los registros
    registrosAcumulados["FaseID"] = []
    registrosAcumulados["FaseEX"] = []
    registrosAcumulados["FaseMEM"] = []
    registrosAcumulados["FaseWB"] = []
    registrosAcumulados["FaseIF"] = []
    parar=False

    while not parar:
        faseWB = FaseWB(bancoDeRegistros, registrosAcumulados,parar,
                        memoriaRegistrosDeAcoplamiento)
        parar=faseWB.iniciar()  # escribe en registros
        faseMEM = FaseMEM(registrosAcumulados, memoria,memoriaRegistrosDeAcoplamiento)
        faseMEM.iniciar()  # escribe o leo en memoria
        faseEX = FaseEX(registrosAcumulados, alu,memoriaRegistrosDeAcoplamiento)
        faseEX.iniciar()  # ejecuta los datos
        faseID = FaseID(registrosAcumulados, bancoDeRegistros,etiquetas)  # lee en registros
        faseID.iniciar()  # devuelve rs y rt
        faseIF = FaseIF(pc, memoriaInstrucciones, registrosAcumulados)
        faseIF.iniciar()  # devuelve el pc y la instruccion leida
        pc=faseIF.getPc()
def iniciarSimulacion():
    f = open('instrucciones.txt', 'r')
    pos=0
    memoria={}
    memoria=Estructura(memoria)
    memoria.iniciar('memoria.txt',"numero")
    memoriaDeInstrucciones={}
    memoriaInstrucciones=MemoriaDeInstrucciones(memoriaDeInstrucciones)
    bancoDeRegistros={}
    bancoDeRegistros=Estructura(bancoDeRegistros)
    etiquetas={}
    etiquetas=Estructura(etiquetas)
    etiquetas.iniciar('etiquetas.txt',"letra")
    bancoDeRegistros.iniciar('bancoDeRegistro.txt',"letra")
    registrosDeAcoplamientoyContenido={}
    registroDeAcoplamientoPorFase={}
    memoriaRegistrosDeAcoplamientoyFinales=MemoriaRegistrosDeAcoplamiento(registrosDeAcoplamientoyContenido,registroDeAcoplamientoPorFase)
    alu=ALU()
    for linea in f:
        linea=linea.strip()
        if(not ':' in linea):#para que no encuentre las etiquetas
            instruccion=crearInstruccion(linea,memoriaRegistrosDeAcoplamientoyFinales)
            memoriaInstrucciones.agregarInstruccion(pos,instruccion)
            pos = pos + 1
    inicio(memoriaInstrucciones,bancoDeRegistros,alu,memoria,0,etiquetas,memoriaRegistrosDeAcoplamientoyFinales)
    print(bancoDeRegistros.getMemoria())
    print(memoria.getMemoria())
iniciarSimulacion()
