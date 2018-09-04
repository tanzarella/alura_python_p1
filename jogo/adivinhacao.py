import random

print("*************************************")
print("* Bem vindo ao jogo de Adivinhação! *")
print("*************************************")

numero_secreto = random.randrange(1, 101)
pontos = 1000
nivel = -1

while nivel < 1 or nivel > 3:
    print("Defina o nível de dificuldade")
    nivel = int(input("(1) Fácil (2) Médio (3) Difícil\n>"))

    if nivel < 1 or nivel > 3:
        print("Você deve digitar um número entre 1 e 3")

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for tentativa in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
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
        print("Você acertou! Sua pontuação foi: ", pontos)
        break
    pontos -= abs(chute - numero_secreto)


print("Fim do jogo")
