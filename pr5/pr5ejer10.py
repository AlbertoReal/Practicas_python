#Alberto Real Gomez: practica 5 ejer 10: piramide

altura=int(input("altura del triangulo"))


for i in range (altura+1):
    print("\n")
    for j in range (altura-i):
        print(" ",end="")
    for k in range ((i*2)-1):
        print ("*",end="")
        


