def llegir_numero():
    return(int(input("Introduce un numero: ")))
def escriure(a):
    suma=0
    for i in range(a,1,-4):
        suma+= i*2
        print("La suma dels quadrats separats entre si es {} es {}".format(a,suma))

a=llegir_numero()
escriure(a)
