def jogar():
    print("*************************************")
    print("*    Bem vindo ao jogo de Forca!    *")
    print("*************************************")

    palavra_secreta = "banana"
    palavra_secreta = palavra_secreta.upper()

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Digite uma letra: ")
        chute = chute.strip()
        chute = chute.upper()

        index = 0
        for letra in palavra_secreta:
                if chute == letra:
                    print("Encontrei a letra {} na posição {}".format(letra,index))
                index += 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()