def superposicio(a, b):
        n = 0
        for e in a:
                n += b.count(e)
        if n>0:
                return[n, True]
        else: 
                return[0, False]

a=input("Introduce la primera lista de elementos como un string, sin espacios: ")
b=input("Introduce la segunda lista de elementos como un string, sin espacios: ")
c, d = superposicio(a,b)
if (c==0):
        print("Las dos listas no tienen nada en comun ")
else:
        print("Las listas tienen ",c, " elementos en comun")