print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))
print("Você digitou: ", chute)

if numero_secreto > chute:
    print("Você errou! O seu chute foi menor que o número secreto.")
elif numero_secreto < chute:
    print("Você errou! O seu chute foi maior que o número secreto.")
else:
    print("Você acertou!")

print("Fim do jogo")
