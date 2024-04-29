##Cria matriz quadrada de espaços
def cria_mapa(N):
    mapa = [[' ' for _ in range(N)] for _ in range(N)]
    return mapa





#Navio pode ser alocado na posição?
def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    # Verifica se a posição inicial está dentro do mapa
    if linha < 0 or coluna < 0 or linha >= len(mapa) or coluna >= len(mapa[0]):
        return False

    # Verifica se a orientação é válida
    if orientacao not in ['v', 'h']:
        return False

    # Verifica se há conflitos com outros navios ou se o navio sai dos limites do mapa
    if orientacao == 'v':
        if linha + blocos > len(mapa):
            return False
        for i in range(linha, linha + blocos):
            if mapa[i][coluna] != ' ':
                return False
    else:
        if coluna + blocos > len(mapa[0]):
            return False
        for j in range(coluna, coluna + blocos):
            if mapa[linha][j] != ' ':
                return False

    return True




#Alocando navios para o computador

import random

def aloca_navios(mapa, blocos):
    def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
        # Verifica se a posição inicial está dentro do mapa
        if linha < 0 or coluna < 0 or linha >= len(mapa) or coluna >= len(mapa[0]):
            return False

        # Verifica se a orientação é válida
        if orientacao not in ['v', 'h']:
            return False

        # Verifica se há conflitos com outros navios ou se o navio sai dos limites do mapa
        if orientacao == 'v':
            if linha + blocos > len(mapa):
                return False
            for i in range(linha, linha + blocos):
                if mapa[i][coluna] != ' ':
                    return False
        else:
            if coluna + blocos > len(mapa[0]):
                return False
            for j in range(coluna, coluna + blocos):
                if mapa[linha][j] != ' ':
                    return False

        return True

    n = len(mapa)

    for navio_blocos in blocos:
        alocado = False
        while not alocado:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])

            if posicao_suporta(mapa, navio_blocos, linha, coluna, orientacao):
                if orientacao == 'v':
                    for i in range(linha, linha + navio_blocos):
                        mapa[i][coluna] = 'N'
                else:
                    for j in range(coluna, coluna + navio_blocos):
                        mapa[linha][j] = 'N'
                alocado = True

    return mapa




#Verifica se acabou os 'N's da matriz
def foi_derrotado(matriz):
    for linha in matriz:
        if 'N' in linha:
            return False
    return True
