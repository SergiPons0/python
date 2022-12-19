def menu():
    print("""
        Menu
        1.Dibuix1
        2. Dibuix2
        3. Adeu
        """)
    opcio=input("Seleccioni el dibuix: ")
    return opcio
def crear_punts(a):
    match a:
        case "1":
            print(""" .  
             . . 
             .   .
              . . 
                .  """)
        case "2":
            print(""" ...
            ...
            ... """)
        case other:
            print("Adeu")
opcio=2
while(opcio!=0):
    opcio = menu()
    crear_punts()
