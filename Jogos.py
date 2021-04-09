import Adivinhacao_com_FOR, forca

def escolhe_jogo():
    print('*'*33)
    print("Escola o Seu Jogo")
    print('*'*33)

    print("(1)Forca (2)Adivinhação")
    jogo = int(input("Qual Jogo?"))

    if jogo == 1:
        print("Jogo da Forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogo da Advinhação")
        Adivinhacao_com_FOR.jogar()


if __name__ == "__main__":
    escolhe_jogo()