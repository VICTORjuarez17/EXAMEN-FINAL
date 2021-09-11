print("-------------------------------------------------------------------------------")
print("---------------------RESOLUCIÓN DE ECUACIONES DE 2° GRADO ---------------------")
print("-------------------------------------------------------------------------------")
print("                       0 = a x**2 + b x + c")
a = float(input("Ingrese el valor numérico del coeficiente 'a': "))
b = float(input("Ingrese el valor numérico del coeficiente 'b': "))
c = float(input("Ingrese el valor numérico del coeficiente 'c': "))

import math

try:
    discri = math.sqrt((b**2)-(4*a*c))
    if discri==0:
        x = (-b)/(2*a)
        print(f"La ecuación tiene soluciones reales e iguales; la solución es {x}")
    else:
        x1 = ((-b)+discri)/(2*a)
        x2 = ((-b)-discri)/(2*a)
        print(f"La ecuación tiene soluciones reales y diferentes; la soluciones son: {x1} y {x2}")
except:
    print("La ecuación no tiene soluciones Reales!")