def invertir(a):
   
   llista=list(a)
   a = llista[::-1]
   # b = str(a)
   return a

a = ("Sergi calvito")
b = invertir(a)
for i in b:
    print(i)