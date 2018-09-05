def jogar():
    print("*************************************")
    print("*    Bem vindo ao jogo de Forca!    *")
    print("*************************************")

    palavra_secreta = "banana"
    palavra_secreta = palavra_secreta.upper()

    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    print(letras_acertadas)

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Digite uma letra: ")
        chute = chute.strip()
        chute = chute.upper()

        index = 0
        for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = chute
                index += 1

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()