def llegir_llista():
    l = [] #Creamos una lista
    for i in range(10): #Hacemos un bucle de 10 elementos, 10 recorridos
        l.append(input()) #append--> afegeix al final de la llista
                            #input--> llegim del teclat
                            #input--> sempre retorna una cadena de caracters "" o ''
    return l

x=llegir_llista()
NumM = 0
for e in x:
    if e[0]== "M":
        NumM+=1
        print("Hay ", NumM, "Palabras que empiezan por M")

