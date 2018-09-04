import forca
import adivinhacao

print("*************************************")
print("*       Bem vindo ao pyjogos        *")
print("*************************************")

jogo = -1

while jogo < 1 or jogo > 2:
    print("Qual jogo deseja jogar?")
    jogo = int(input("(1) Forca (2) Adivinhação\n>"))

    if jogo < 1 or jogo > 2:
        print("Você deve digitar um número entre 1 e 2")

if (jogo == 1):
    forca.jogar()
else:
    adivinhacao.jogar()
