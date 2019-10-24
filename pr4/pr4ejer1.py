#Alberto Real Gomez: practica 4 ejer 2: cual es el mayor y el menor

num_1 = int(input("primero numero\n"))
num_2 = int(input("segundo numero\n"))
num_3 = int(input("tercero numero\n"))
num_4 = int(input("cuarto numero\n"))
num_5 = int(input("quinto numero\n"))
maximo = 0

if num_2> num_1:
    maximo=num_2
    print(maximo,"1")
elif num_3> num_2:
    maximo=num_3
elif num_4> num_3:
    maximo=num_4
elif num_5> num_4:
    maximo=num_5
    print("5")

