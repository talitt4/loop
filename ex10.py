usuario_palavra = input("entre com uma palavra: ")
usuario_palavra = usuario_palavra.upper()

for letra in usuario_palavra:
    if letra == "A":
        continue 
    elif letra == "E":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
       palavra_sem_vogais += letra
       
print(palavras_sem_vogais)