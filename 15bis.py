
def sumar_llista(a):
    sumatori=0

    for i in a:
        sumatori += (i*i)
    return sumatori

def multiplicar_llista(a):
    multiplicado=1
    for i in a:
        multiplicado *=1
    return multiplicado 

x = [1, 2, 3, 4, 5]
print("La suma dels elements de la llista és: ", sumar_llista(x))
print("La multiplicacio dels elements de la llista és: ", multiplicar_llista(x))