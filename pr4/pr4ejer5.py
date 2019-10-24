#Alberto Real Gomez: practica 4 ejer 5: cajero

entrada = int(input("dinero a retirar"))

if entrada == 500 or entrada%500==0:
    valor = int( entrada/500)
    print (valor,"billetes de 500")
elif entrada ==200 or entrada%200==0:
    valor = int(entrada/200)
    print (valor, "billetes de 200")
elif entrada ==100 or entrada%100==0:
    valor = int(entrada/100)
    print (valor, "billetes de 100")
elif entrada ==50 or entrada%50==0:
    valor = int(entrada/50)
    print (valor, "billetes de 50")
elif entrada ==20 or entrada%20==0:
    valor = int(entrada/20)
    print (valor, "billetes de 20")
elif entrada ==10 or entrada%10==0:
    valor = int(entrada/10)
    print (valor, "billetes de 10")
elif entrada ==5 or entrada%5==0:
    valor = int(entrada/5)
    print (valor, "billetes de 5")
else:
    print ("el cajero no dispone de billetes para el valor introducido")
