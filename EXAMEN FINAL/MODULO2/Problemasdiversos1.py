n = int(input("Ingrese la cantidad de alumnos a registrar : "))
lista_alumnos = []
for i in range(n):
    dicx_alumnos = {}
    dicx_alumnos['alumno'] = input(f'Ingrese el {i+1} alumno: ')
    nota1 = int(input('ingrese la nota 1: '))
    nota2 = int(input('ingrese la nota 2: '))
    nota3 = int(input('ingrese la nota 3: '))
    dicx_alumnos['notas'] = [nota1,nota2,nota3]
    lista_alumnos.append(dicx_alumnos)
print(lista_alumnos)