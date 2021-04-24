# n o número de peças inicial
# m o número máximo de peças que é possível retirar em uma rodada.


def computador_escolhe_jogada(n, m):
    if m == n:
        jogada_computador = n
    elif (n % (m + 1)):
        jogada_computador = (n % (m + 1))
    else:
        jogada_computador = m

    if jogada_computador == 1:
        print("\nO computador tirou uma peça.")
    else:
        print(f"\nO computador tirou {jogada_computador} peças.")
    return jogada_computador


def usuario_escolhe_jogada(n, m):
    while True:
        try:
            jogada_usuario = int(input("\nQuantas peças você vai tirar? "))
            while jogada_usuario > m or jogada_usuario > n or jogada_usuario <= 0:
                print("\nOops! Jogada inválida! Tente de novo.")
                jogada_usuario = int(input("\nQuantas peças você vai tirar? "))

            if jogada_usuario == 1:
                print("\nVocê tirou uma peça.")
            else:
                print(f"\nVocê tirou {jogada_usuario} peças")
            break
        except ValueError:
            print("\nOops! Jogada inválida! Tente de novo.\n")

    return jogada_usuario


def partida():
    # Definição de quantas peças e limites por rodada
    # Definição de quem começa o jogo

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if (n % (m + 1)) == 0:  # Jogador começa
        print("\nVoce começa!")
        usuario_comeca = True
    else:  # Computador começa
        print("\nComputador começa!")
        usuario_comeca = False


    while n > 0:
        if usuario_comeca:
            # Jogador joga
            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada

            usuario_comeca = False
        else:
            # Computador joga
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            usuario_comeca = True

        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        elif n != 0:
            print(f"Agora restam {n} peças no tabuleiro.")

    if usuario_comeca:
        print("Fim de jogo! O computador ganhou!\n")
        return 0
    else:
        print("Fim de jogo! Você ganhou!\n")
        return 1


def campeonato():
    rodada = 1
    pontos_computador = 0
    pontos_usuario = 0

    while rodada <= 3:
        print(f"**** Rodada {rodada} **** \n")
        ponto = partida()
        rodada += 1

        if ponto == 1:
            pontos_usuario += 1
        else:
            pontos_computador += 1

    print(f"\nPlacar: Você {pontos_usuario} X {pontos_computador} Computador")



# Começo e Escolha do metodo de jogo
print("Bem-vindo ao jogo NIM! Escolha:")
metodo_de_jogo = 0
while not metodo_de_jogo == 1 or metodo_de_jogo == 2:
    metodo_de_jogo = int(input("1 - para jogar uma partida isolada\n"
      "2 - para jogar um campeonato "))

    if metodo_de_jogo == 1:
        print("\nVoce escolheu uma partida isolada!\n")
        partida()
    elif metodo_de_jogo == 2:
        print("\nVoce escolheu um campeonato!\n")
        campeonato()
    else:
        print("\nEscolha 1 ou 2!")



