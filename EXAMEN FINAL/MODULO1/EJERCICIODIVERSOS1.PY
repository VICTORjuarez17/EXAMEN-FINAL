print("---------------------------------------------------------------------------------")
print("                                   'Banco'")
print("---------------------------------------------------------------------------------")
r = 4
cantidad = float(input("Ingrese la cantidad de dinero que desea depositar en su cuenta de ahorros: "))
for i in range(3):
    monto = cantidad * (1+((r*(i+1))/100))
    print(f'Su capital acumulado en el {i+1}° Año es: {monto}')