print("--------------Verificación de Tarjetas ----------------")
num_tarjeta = input("Ingrese su número de Tarjeta: ")
num_tarjeta_dos = num_tarjeta[-2::-2]
sum1cif = 0
sum2cif = 0
for i in num_tarjeta_dos:
    nuevo_num = int(i)*2
    sum3cif = 0
    if nuevo_num >=10:
        for l in str(nuevo_num):
            sum3cif += int(l)
        sum2cif += sum3cif
    else:
        sum1cif +=nuevo_num
    suma_total = sum1cif + sum2cif
num_tarjeta_tres = num_tarjeta[-1::-2]
sumimpar = 0
for m in num_tarjeta_tres:
    sumimpar += int(m)
suma_total2 = suma_total + sumimpar
if (suma_total2 % 10)==0:
    print("Su tarjeta es válida!")
    if (int(num_tarjeta[0:2:1])==34) or (int(num_tarjeta[0:2:1])==37):
        print("Su tarjeta es AMEX")
    elif (int(num_tarjeta[0:2:1])>=51) and (int(num_tarjeta[0:2:1])<=55):
        print("Su tarjeta es MASTERCARD")
    elif (int(num_tarjeta[0:1:1])==4):
        print("Su tarjeta es VISA")
    else:
        print("Su tarjeta no pertenece al rango de conocidas")
else:
    print("Su tarjeta no es válida!!!")
