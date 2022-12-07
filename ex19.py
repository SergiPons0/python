def crear_repetits(a,b):
    c = b*int(a)
    return c

a =input("Afegeix un numero de repeticions: ")
b =input("Afegeix el caracter a repetir: ")
print("El caracter ",b," repetit ",a," vegades es: ",crear_repetits(a,b))
