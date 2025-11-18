import random

# FUNÇÕES 

def criar_tabuleiro():
    tabuleiro = [['_' for _ in range(10)] for _ in range(10)]
    return tabuleiro

def colocar_itens(tabuleiro):
    posicoes = [(linha, coluna) for linha in range(10) for coluna in range(10) if not (linha == 0 and coluna == 0)]
    random.shuffle(posicoes)

    # Tesouro
    t_linha, t_coluna = posicoes.pop()
    tabuleiro[t_linha][t_coluna] = 'T'

    # Armadilhas
    for _ in range(random.randint(3, 6)):
        linha, coluna = posicoes.pop()
        tabuleiro[linha][coluna] = 'A'

    # Pistas
    for _ in range(random.randint(5, 8)):
        linha, coluna = posicoes.pop()
        tabuleiro[linha][coluna] = 'P'

def mostrar_tabuleiro(tabuleiro, revelado):
    print("\nTabuleiro:")
    for linha in range(10):
        for coluna in range(10):
            if revelado[linha][coluna]:
                print(tabuleiro[linha][coluna], end=" ")
            else:
                print("X", end=" ")
        print()

def dica(t_linha, t_coluna, linha, coluna):
    msg = "Dica: o tesouro está "
    
    if linha > t_linha:
        msg += "acima "
    elif linha < t_linha:
        msg += "abaixo "
    
    if coluna > t_coluna:
        msg += "e à esquerda."
    elif coluna < t_coluna:
        msg += "e à direita."

    print(msg)

def encontrar_tesouro(tabuleiro):
    for linha in range(10):
        for coluna in range(10):
            if tabuleiro[linha][coluna] == 'T':
                return linha, coluna

# JOGO

def jogar():
    tabuleiro = criar_tabuleiro()
    colocar_itens(tabuleiro)
    revelado = [[False]*10 for _ in range(10)]
    t_linha, t_coluna = encontrar_tesouro(tabuleiro)

    print("Bem-vindo ao jogo Caça ao Tesouro!")

    while True:
        mostrar_tabuleiro(tabuleiro, revelado)

        try:
            linha = int(input("Linha (0-9): "))
            coluna = int(input("Coluna (0-9): "))
        except:
            print("Digite apenas números.")
            continue

        if not (0 <= linha < 10 and 0 <= coluna < 10):
            print("Essa posição não existe.")
            continue

        if revelado[linha][coluna]:
            print("Você já tentou essa posição.")
            continue

        revelado[linha][coluna] = True
        item = tabuleiro[linha][coluna]

        if item == 'T':
            mostrar_tabuleiro(tabuleiro, revelado)
            print("\n🎉 Você encontrou o tesouro! Parabéns!")
            break

        elif item == 'A':
            mostrar_tabuleiro(tabuleiro, revelado)
            print("\n💀 Você caiu em uma armadilha! Game Over.")
            break

        elif item == 'P':
            print("\n🔍 Você encontrou uma pista!")
            dica(t_linha, t_coluna, linha, coluna)

        else:
            print("\nErrou, continue tentando ...")

# Iniciar o jogo
jogar()