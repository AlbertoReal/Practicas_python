#Alberto Real Gomez: practica 5 ejer 2: imprimir

entrada1 = int(input("primer valor\n"))
entrada2 = int(input("segundo valor\n"))

for i in range (entrada1,entrada2+1):
    if i%2==0:
        print ("este numero es par",i)
    else:
        print ("este numero es impar",i)
