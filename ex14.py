def vocal(a):

    if(a=='a' or a=='A' or a=='e' or a=='E' or a=='i' or a=='I' or a=='o' or a=='O' or a=='u' or a=='U'):
        return True
    else:
        return False
    
    
a=input("Introduzca un caracter: ")
print("La funció ens indica si és vocal o consonant:",vocal(a))


