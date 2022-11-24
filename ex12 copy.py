def gran_de_tres(x,y,z):
    a=z
    if(x>y):
        if(x>z): # x>y and x>z
            a=x
        elif (z>x):# x>y and z > x => z és el major
            a=z
        else: #Aqui x = z > y => x,z són els majors
            a=x 
    elif (y>x): # y>x
        if (y>z): #y>x and y>z => z es el major
            a=y
        elif(z>y): #y
            a=z
        else: #Aqui y > x and z=y ==
            a=y
    else: #x=y
        if (x>z): # x=y and x=z
            a=x
        elif (z>x): #x=y and z>x ==> z és el major
            a=z
        else: #x=y=z ==> x,y,z són iguals
            a=x
    return a 

# Aplicació principal
a=int(input("Numero 1: "))
b=int(input("Numero 2: "))
c=int(input("Numero 3: ")) 
d=gran_de_tres(a,b,c)
print("El major de ",a,",",b,",",c,"és ",d)