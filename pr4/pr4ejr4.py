#Alberto Real Gomez: practica 4 ejer 4: area triangulo o cuadradoes divisor

num_1 = int(input("primero numero"))
num_2 = int(input("segundo numero"))
num_3 = int(input("tercero numero"))
divisor = int(input("introduce el divisor"))

if num_1%divisor ==0 and num_2%divisor ==0 and num_3%divisor ==0:
    print ("los numeros introducidos son divisibles por el divisor")
else:
    print ("todos los numeros introducidos no son divisibles por el divisor")
