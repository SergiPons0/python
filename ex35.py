def llegir_paraula():
    return (input("Introduce una palabra: "))

def comparar(a,b):
    if a == b:
        print("Son la mateixa paraula, per aço riman")
    elif a[-3:] == b[-3:]:
        print("Les paraules rimen")
    elif a[-2:] == b[-2:]:
        print("Les paraules rimen un poc")
    elif a[-1:] == b[-1:]:
        print("Les paraules rimen molt poc")
    else: 
        print("No rimen res")