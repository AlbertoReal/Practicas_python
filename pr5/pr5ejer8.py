#Alberto Real Gomez: practica 5 ejer 7: trinagulo inverso

altura=int(input("anchura del triangulo"))



for i in reversed(range (altura+1)):
    print("\n")
    for j in range (i):
        print ("*",end="")
