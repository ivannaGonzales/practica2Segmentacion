probando=["$s0",True]
probandoArray=[["$s1",True],["$s0",True],["$t3",False]]
probandoOtraVez="$s0"
print(probandoOtraVez in probandoArray)
for i in probandoArray:
    tupla=i
    final=False
    if(tupla==probandoOtraVez):
        final=True
print(probandoArray)
indice=probandoArray.index(probando)
dameTuplaParaCambiar=probandoArray[indice]
#lo elimino
probandoArray.remove(dameTuplaParaCambiar)
dameTuplaParaCambiar=["$s0",False]
probandoArray.insert(indice,dameTuplaParaCambiar)
print(indice)
print(probandoArray)