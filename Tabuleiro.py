Letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# alfabeto para montar o nome das colunas
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def mapa_matrix(n):
    matrix = []
    for a in range(n):
        matrix.append([" "]*n)
    return matrix  

