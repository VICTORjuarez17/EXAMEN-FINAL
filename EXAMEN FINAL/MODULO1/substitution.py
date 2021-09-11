print("--------------------------------------------------------")
print("               'Substitución.py'")
print("--------------------------------------------------------")
linea_com = input("Ingrese su línea de Comandos: ")
linea_coman = linea_com.lower()
abcdario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
if (linea_coman.isalpha()) and ( len(linea_coman) ==26):
    cant = []
    for ip in linea_coman:
        alm = linea_coman.count(ip)
        cant.append(alm)
        for jt in cant:
            if jt !=0:
                plaintext: print('Ingrese el texto a convertir: ')
                ciphertext =[]
                dicc = {}
                c1 = []
                c2 = []
                for mp in linea_coman:
                    val = abcdario.index((linea_coman.index(mp)))
                    c1.append(val)
                    c2.append(mp)
                dicc = {c1:c2}

                for lk in plaintext:
                        letra = dicc[lk]
                        ciphertext.append()
            else:
                print("Error 1")
else:
    print("Error 1")