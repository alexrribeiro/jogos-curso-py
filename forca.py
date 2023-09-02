def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "laranja".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            # erros_restantes = 6 - erros
            # print(f"Faltam {erros_restantes} erros para você ser enforcado!")
            print("Faltam {} erros para você ser enforcado".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print("Parabéns! Você acertou!")
    else:
        print("Que pena! Você perdeu!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
