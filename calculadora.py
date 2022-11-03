print("""
Menú:
1. Sumar
2. Resta
3. Multiplicar
4. Dividir
0. Sortir
""")
opcio=input("Seleccioni l'opcio que vulgui: ")
a = input("Indiqui el primer operand: ")
b = input("Indiqui el segon operand: ")
match opcio:
    case "1":
        c=int(a)+int(b)
        print("La suma de ",a," més ",b," és ",c) 
    case "2":
        c=int(a)-int(b)
        print("La resta de ",a," menys ",b," és ",c)
    case "3":
        c=int(a)*int(b)
        print("La multipicació de ",a," per ",b," és ",c)
    case "4":
        c=int(a)/int(b)
        print("La divisió de ",a," partit ",b," és ",c)
    case "0":
        print("Adeu!")
    case other:
        print("Opcio no vàlida!")