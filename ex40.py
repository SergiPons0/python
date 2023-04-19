def llegir_numero():
    return (int(input("Introduce un numero: ")))
def taula_multiplicar(a):
    for i in range (21):
        print("{} * {} = {} ".format(i,a,i*a))

#PP
a=llegir_numero()
taula_multiplicar(a)