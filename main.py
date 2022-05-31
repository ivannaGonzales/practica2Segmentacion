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
    if(tipo=="add" or tipo=="sub"):
        rd=registros[0]
        memoriaRegistrosDeAcoplamientoyFinales.agregarRegistroFinal(rd)
        rs=registros[1]
        rt=registros[2]
        instruccion=TipoR(tipo,rs,rt,rd)
    elif(tipo=="sw"or tipo=="lw"):
        rt=registros[0]
        memoriaRegistrosDeAcoplamientoyFinales.agregarRegistroFinal(rt)
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


def iniciarNotengoNiIdea(memoriaInstrucciones, bancoDeRegistros, alu, memoria, pc, etiquetas,memoriaRegistrosDeAcoplamiento):
    i = 0
    registrosAcumulados = {}  # se va acumulando todos los registros
    registrosAcumulados["FaseID"] = []
    registrosAcumulados["FaseEX"] = []
    registrosAcumulados["FaseMEM"] = []
    registrosAcumulados["FaseWB"] = []
    registrosAcumulados["FaseIF"] = []
    parar=False
    #puedo tener algo asi como, una memoria de registros que sean destino, entonce
    while i <= len(memoriaInstrucciones.getMemoriaDeInstrucciones()) and not parar:
        faseWB = FaseWB(bancoDeRegistros, registrosAcumulados,parar,memoriaInstrucciones.getMemoriaDeInstrucciones(),
                        memoriaRegistrosDeAcoplamiento)#acaba cuanfo el acaba
        parar=faseWB.iniciar()  # escribe en registros
        faseMEM = FaseMEM(registrosAcumulados, memoria,memoriaRegistrosDeAcoplamiento)
        faseMEM.iniciar()  # escribe o leo en memoria
        faseEX = FaseEX(registrosAcumulados, alu,memoriaRegistrosDeAcoplamiento,memoriaInstrucciones)
        faseEX.iniciar()  # ejecuta los datos
        faseID = FaseID(registrosAcumulados, bancoDeRegistros,etiquetas)  # lee en registros
        faseID.iniciar()  # devuelve rs y rt
        faseIF = FaseIF(pc, memoriaInstrucciones, registrosAcumulados)
        registros=faseIF.iniciar()  # devuelve el pc y la instruccion leida
        i=registros[1]-1#i es igual al pc, espero
def iniciarSimulacion():
    f = open('instrucciones.txt', 'r')
    pos=0
    memoria={}
    memoria=Memoria(memoria)
    memoria.iniciar()
    memoriaDeInstrucciones={}
    memoriaInstrucciones=MemoriaDeInstrucciones(memoriaDeInstrucciones)
    bancoDeRegistros={}
    bancoDeRegistros=BancoDeRegistros(bancoDeRegistros)
    etiquetas={}
    etiquetas=MemoriaDeEtiquetas(etiquetas)
    etiquetas.iniciarMemoriaDeEtiquetas()
    bancoDeRegistros.iniciarbancoDeRegistros()
    memoriaRegistrosFinales=[]
    memoriaRegDeAcoplamiento=[]
    registrosDeAcoplamientoyContenido={}
    registroDeAcoplamientoPorFase={}
    memoriaRegistrosDeAcoplamientoyFinales=MemoriaRegistrosDeAcoplamiento(memoriaRegistrosFinales,memoriaRegDeAcoplamiento,registrosDeAcoplamientoyContenido,registroDeAcoplamientoPorFase)
    alu=ALU()
    for linea in f:
        linea=linea.strip()
        if(not ':' in linea):#para que no encuentre las etiquetas
            instruccion=crearInstruccion(linea,memoriaRegistrosDeAcoplamientoyFinales)
            memoriaInstrucciones.agregarInstruccion(pos,instruccion)
            pos = pos + 1
    iniciarNotengoNiIdea(memoriaInstrucciones,bancoDeRegistros,alu,memoria,0,etiquetas,memoriaRegistrosDeAcoplamientoyFinales)
iniciarSimulacion()
