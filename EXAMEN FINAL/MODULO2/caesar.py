import string
abecedario = string.ascii_uppercase
k = 13
plaintext = "Mi mama me MiMA"
ciphertext = ""
for m in plaintext:
    if m.upper() not in abecedario:
        ciphertext = ciphertext + m
        continue
    w = (abecedario.find(m.upper()) + k) %26
    if m.isupper():
          x = abecedario[w]
    else:
        x = abecedario[w].lower()
    ciphertext = ciphertext + x
    
print(ciphertext)