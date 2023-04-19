import random

def calculem_n_aleatoris():
    b=[]
    for i in range(4):
        b.append(random.randint(0,9))
    return b

def llegir_usuari():
    b=[]
    for i in range (4):
        b.append(int(input("Introdueix un nombre: ")))
    return b

def comparar(a,b):
    a, b, c=0
    for i in range (4):
        if a[i] == b[i]:
             a+=1
        elif b[i] in a:
            b+=1
        else:
            c+=1
        if a==4:
            print("Muy bien, has adivinado el numero{}".format())
            return 1
        elif a>0 and b>0:
            print("Has adivinado {} y {} estan pero no en su posicion correcta ".format(a,b))
            return 0
        elif a==4 and b>0:
            print("Has adivinado {} y {} estan pero no en su posicion correcta" .format(a,b))
            return 0
        elif a>0 and b==0:
            print("Has adivinado {} y {} estan pero no en su posicion correcta" .format(b))
            return 0
        else:
            print("No has encertat res")
            return 0


#PP
a= calculem_n_aleatoris()
sortir=0
while sortir!=1:
    b=llegir_usuari()
    if comparar(a,b)==1:
        sortir=1
    else:
        sortir=0
   

