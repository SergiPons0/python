
def menu():
    print("""
    1. Ruleta Aleatoria
    2. Juego de Adivinanzas
    3. efe
    4. fefef
    5. ddwed
    """)
    x= input("Introduce una opcion del menu: ")
    return x

def adivinanzas():
    print("""
    -Soy un ave muy colorida,
    Con plumas brillantes y largas,
    En las noches, mi canto es oído,
    ¿Quién soy? Soy el Pavo real.

    -Tengo ramas, pero no hojas,
    Un tronco, pero no es de árbol,
    ¿Qué soy? Soy una Silla.

    -De noche soy blanco,
    De día me vuelvo negro,
    ¿Quién soy? Soy el Búho.

    -Todos me quieren tocar,
    Pero si me tocan, me destruyen,
    ¿Quién soy? Soy el Hielo.

    *La respuesta tiene que estar contestada con la primera letra mayuscula
    """)
a=input("Respuestas 1: ")
b=input("Respuestas 2: ")
c=input("Respuestas 3: ")
d=input("Respuestas 4: ")
if a=="Pavo real":
    print("La respuesta 1 es correcta ")
if not a=="Pavo real":
    print("La respuesta 1 es incorrecta ")
if b=="Silla":
    print("La respuesta 2 es correcta ")
if not b=="Silla":
    print("La respuesta 2 es incorrecta ")
if c=="Buho":
    print("La respuesta 3 es correcta ")
if not c=="Buho":
    print("La respuesta 3 es incorrecta ")
if d=="Hielo":
    print("La respuesta 4 es correcta ")
if not d=="Hielo":
    print("La respuesta 4 es incorrecta ")
else:
    print("Gracias por jugar")


x="1"
while x!=("."):
    if x!=("."):
        x = menu()
    match x:
        case "1":
            print("Has elejido la opcion de la ruleta aleatoria" )
            Ruleta=ruleta_aleatoria()

        case "2":
            print("Has elejido la opcion de el juego de las adivinanzas")
            Juego=adivinanzas()
        case "3":
            print("Has elejido la opcion de emjfeifj")
            eje=ejeje()
        case "4":
            print("Has elejido la opcion de la fefefe")
            lala=lalalala()
        case "5":
            print("Has elejido la opcion de la ddwed")
            poka=pokapoka()
        case other:
            print("Opcion no valida")


    












