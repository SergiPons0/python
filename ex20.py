def crear_repetits(a,b):
    c = b*int(a)
    return c

def crear_punts(a):
    for e in a:
        c=crear_repetits(int(e),'.')
        print(c)
    
a= input("Escibe una lista de numeros de elementos: ")
crear_punts(a)

