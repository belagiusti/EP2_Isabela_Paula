Letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
import random
import constantes

def mapa_matrix(n):
    matrix = []
    for a in range(n):
        matrix.append([" "]*n)
    return matrix  

def suporta_bloco (mapa, blocos, linha, coluna, sentido):

    if sentido =="h":
        if (coluna)+blocos > len(mapa(coluna[linha])):
            return False
    elif sentido =="v":
        if (linha)+blocos > len(mapa[linha]):
            return False    
        
    for i in range(blocos):
        if sentido == "h":
            if mapa[linha][coluna+i] == "N":
                return False
            
        elif sentido == "v":
            if mapa[linha+i][coluna] == "N":
                return False
    return True

def aloca_navios (mapa, listablocos):
    for i in range(len(listablocos)):
        pode = False
        
    while pode == False:
        linha = random. randint(0, (len (mapa) -1))
        coluna = random. randint(0, (len(mapa)-1))
        sentido = random. choice(['h', 'v'])
        pode = suporta_bloco(mapa, listablocos[i], linha, coluna, sentido)
    
    mapa = navio_jogador (mapa, listablocos[i], linha, coluna, sentido)
    return mapa

def navio_jogador (mapa, navio, linha, coluna, sentido):
    for x in range (navio):
        if sentido == "h":
            mapa[linha][coluna+x] == "N"
        else:
            mapa[linha+x][coluna] = "N"
    return mapa

def derrotado(matrix):
    for z in matrix:
        for j in z:
            if j =="N":
                return False
    return True

def printando_mapas(matrix_comp, matrix_jogador):
    print("\n")
    print("               MAPA COMPUTADOR                                     MAPA JOGADOR")
    print("  A   B   C   D   E   F   G   H   I   J               A   B   C   D   E   F   G   H   I   J   ")
    for i_lista in range(len(matrix_comp)):
        linha = ""
        linha+= str(i_lista + 1)
        for info in range(len(matrix_comp[i_lista])):
            if matrix_comp[i_lista][info] == 'X':
                if i_lista == 9 and info==0:
                    linha+= ("   "+"\u001b[33m"+(matrix_comp[i_lista][info])+'\u001b[0m')
            