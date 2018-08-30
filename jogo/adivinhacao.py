print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
tentativa = 1

while tentativa <= total_de_tentativas:
    print("Tentativa {} de {}".format(tentativa,total_de_tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou: ", chute)
    
    if numero_secreto > chute:
        print("Você errou! O seu chute foi menor que o número secreto.")
    elif numero_secreto < chute:
        print("Você errou! O seu chute foi maior que o número secreto.")
    else:
        print("Você acertou!")
        tentativa = total_de_tentativas

    tentativa += 1
    
print("Fim do jogo")
