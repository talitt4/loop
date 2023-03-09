numero_secreto = 42
tentativa = 1

while tentativa <= 3:
    palpite = int(input("Adivinhe o número secreto:"))
    if palpite == numero_secreto:
        print ("Parabéns, voce acertou!")
        break 
    else:
        if palpite > numero_secreto:
            print("O numero secreto é menor que", palpite)
        else:
            print("O número secreto é maior que", palpite)
    tentativa += 1
    
if tentativa > 3:
    print("Suas tentativas acabaram. O número secreto era", numero_secreto)
    