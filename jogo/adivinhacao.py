import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
tentativa = 1


for tentativa in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(tentativa,total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))

    if chute < 1 or chute > 100:
        print("Você digitou {}, você deve digitar um número entre 1 e 100".format(chute))
        continue
    else:
        print("Você digitou: ", chute)
    
    if numero_secreto > chute:
        print("Você errou! O seu chute foi menor que o número secreto.")
    elif numero_secreto < chute:
        print("Você errou! O seu chute foi maior que o número secreto.")
    else:
        print("Você acertou!")
        break
    
print("Fim do jogo")
