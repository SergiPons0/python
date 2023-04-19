def llegir_numero():
    return(int(input("Introduce un valor: ")))
def llegir_numero_float():
    return(float(input("Introduce un valor real: ")))
def calcular_prestec(q,i,a):
    return (q*(1+i/100)**a)



#PP
q=llegir_numero()
i=llegir_numero_float()
a=llegir_numero()
c=calcular_prestec(q,i,a)
print("Si sol·licito {} a un interes anual del {} a {} anys, al final pagare {} euros".format(q,i,a,c))