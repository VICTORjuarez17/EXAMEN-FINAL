print("------------------------------------------------------------------------")
print("                        'Mario Plays'           ")
print("------------------------------------------------------------------------")
num_lineas = int(input("Indique la altura de su pirámide: "))
while (num_lineas<=0) or (num_lineas>8):
    print("La altura de la pirámide es inválida!")
    num_lineas = int(input("Indique la altura de su pirámide: "))
else:
    espacio = list(range(num_lineas))
    for i in espacio:
        print(" "*(num_lineas-(i+1))+"#"*((i+1)))