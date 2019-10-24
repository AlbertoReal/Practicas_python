#Alberto Real Gomez: practica 5 ejer 12: primos

multiplos=int(input("valor de entrada"))
no_primo=False

for i in range (multiplos+1):
    if i>=1 and i<multiplos-1:
        if i>1 and multiplos%i==0:
             no_primo=True
if no_primo==True:
    print("no es primo")
else:
    print ("es primo")
        
            
