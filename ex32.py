def any_bisiesto(x):
    if x%4==0 and (x%400>0 or x%100==0):
        print("Es año bisiesto")
    else:
        print("No es bisiesto")

#PP
b=input("Introduce un año: ")
any_bisiesto(int(b))
