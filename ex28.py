def llegir():
    llista=[]
    a='a'
    while a!='.':
        a=input("Introdueix un numero: ")
        if a!='.':
            llista.append(int(a))
    return tuple(llista)


def mostrar_major_que(a,num):
    for e in a:
        if e>num:
            print(e)
    
x=llegir()
i=input("Introdueix el numero que vol comparar: ")
mostrar_major_que(x,int(i))
