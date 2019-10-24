#Alberto Real Gomez: practica 5 ejer 8: trinagulo ancho

entrada1=int(input("altura del rectangulo"))
entrada2=int(input("lado del rectangulo"))

for i in range (entrada1):
    if i==0:
         for j in range (entrada2):
            print("*",end="")
    elif i==entrada1-1:
        for j in range (entrada2):
            print("*",end="")
    else:
        for j in range (entrada2):
            if j==0:
                print("*",end="")
            elif j==entrada2-1:
                print("*",end="")
            else:
                print(" ",end="")
        
    print ("\n")
   

        
