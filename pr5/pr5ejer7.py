#Alberto Real Gomez: practica 5 ejer 8: trinagulo ancho

altura=int(input("anchura del triangulo"))


for i in range (altura+1):
    print("\n")
    for j in range (i):
        print ("*",end="")

for i in reversed(range (altura+1)):
    print("\n")
    for j in range (i):
        print ("*",end="")
