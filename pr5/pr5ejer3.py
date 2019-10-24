#Alberto Real Gomez: practica 5 ejer 2: imprimir

entrada1 = int(input("primer valor\n"))
entrada2 = int(input("segundo valor\n"))
aux=entrada1
for i in range (entrada1,entrada2):
    print (i,"h")
    aux=aux+i+1
    print (aux)
print ("valor final",aux)
