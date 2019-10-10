#Alberto Real Gomez: practica 3 ejer 7: fechas correctas

dia = int(input ("introduce el dia"))
mes = int(input("introduce el mes"))
year = int(input("introduce el año"))

if dia<1 or dia >31:
    print ("dia incorrecto")
elif mes<1 or mes>12:
    print("mes incorrecto")
elif mes ==2 and dia>28:
    print ("dia incorrecto")
elif mes==4 or mes==6 or mes==9 or mes==11 and dia>30:
    print ("dia incorrecto")
else:
    print ("fecha correcta")
