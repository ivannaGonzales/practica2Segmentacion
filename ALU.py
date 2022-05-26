class ALU():
    def __init__(self):
        pass
    def getResultado(self,op1,op2,op):
        op1=int(op1)
        op2=int(op2)
        if(op=="suma"):
            resultado=op1+op2
        elif(op=="resta"):
            resultado=op1-op2
        return resultado