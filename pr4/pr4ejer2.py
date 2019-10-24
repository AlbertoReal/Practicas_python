#Alberto Real Gomez: practica 4 ejer 2: cual es el mayor

num_1 = int(input("primero numero"))
num_2 = int(input("segundo numero"))
num_3 = int(input("tercero numero"))
num_4 = int(input("cuarto numero"))
num_5 = int(input("quinto numero"))

if num_1<num_2 and num_2<num_3 and num_3<num_4 and num_4<num_5:
    print("orden ascendente")
elif num_1>num_2 and num_2>num_3 and num_3>num_4 and num_4>num_5:
    print ("orden descendente")
else:
    print ("desordenado")
