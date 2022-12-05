def longitud(valor):
    
    if type(valor) is not list and type(valor) is not str:
        return -1
 
    contador = 0
   
    for elemento in valor:
        contador += 1
    return contador



cadena = "wese"
print("Longitud de cadena:", longitud(cadena))
cadena = "epicureo"
print("Longitud de cadena:", longitud(cadena))
lista = ["bolivar"]
print("Longitud de lista:", longitud(lista))



