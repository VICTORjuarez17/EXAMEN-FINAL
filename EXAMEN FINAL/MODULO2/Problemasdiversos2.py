n = int(input('¿Cuántos alumnos desea registrar?: '))
alumnos = []
for i in range(n):
    alumn_dicc = {}
    nombre = input("Ingrese el nombre del Alumno: ")
    sum_acum=0
    prome = []
    nombres = []
    cond = []
    for j in range(3):
        nota = float(input(f'Ingrese su {j+1}° Nota: '))
        if (nota>=0) and (nota<=10):
            sum_acum += nota
        else:
            print("La nota ingresada no es válida")
    prom = round(sum_acum/3,2)
    if prom>=4:
        condicion = "Aprobado"
    else:
        condicion = "Desaprobado"
    prome.append(prom)
    nombres.append(nombre)
    cond.append(condicion)
    alumn_dicc["Alumnos"]= nombres
    alumn_dicc["Nota Final"]= prome
    alumn_dicc["Condición"]=cond
    alumnos.append(alumn_dicc)
print(alumnos)