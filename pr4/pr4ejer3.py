#Alberto Real Gomez: practica 4 ejer 3: area triangulo o cuadrado

tipo_area = input("introduce si se trata de un cuadrado o un triangulo\n")
lado_1 = int(input("primer lado\n"))
lado_2 = int(input("segundo lado\n"))

if tipo_area =="cuadrado":
    area_cuad = lado_1 * lado_2
    print("el area del cuadrado es",area_cuad)
elif tipo_area =="triangulo":
    area_tria = (lado_1 * lado_2)/2
    print ("el area del triangulo es",area_tria)
else:
    print ("introduce tipo de area 'cuadrado o triangulo'")
                  
