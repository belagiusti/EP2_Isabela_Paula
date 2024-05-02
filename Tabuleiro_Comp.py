
PAISES =  { 
    1:{
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }},
      2:{
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    }},
    3:{
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    }},
    4:{
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    }},
    5:{
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }}
}

dic_mapa_comp= {
    'letra': ['A','B','C','D','E','F','G','H','I','J'],
    '1': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','1'],
    '2': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','2'],
    '3': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','3'],
    '4': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','4'],
    '5': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','5'],
    '6': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','6'],
    '7': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','7'],
    '8': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','8'],
    '9': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','9'],
    '10': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','10'],
    'letra2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
}
dic_mapa = {
    'letra': ['A','B','C','D','E','F','G','H','I','J'],
    '1': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','1'],
    '2': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','2'],
    '3': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','3'],
    '4': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','4'],
    '5': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','5'],
    '6': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','6'],
    '7': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','7'],
    '8': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','8'],
    '9': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','9'],
    '10': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','10'],
    'letra2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
}



print("           MAPA COMPUTADOR                   ") #Imprime nome do mapa
print("   " + "  ".join(dic_mapa_comp['letra']))  # Imprime a linha de letras
for i in range(1, 11):
    linha = dic_mapa_comp[str(i)]  # Pega a linha correspondente do dicionário
    print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
print("   " + "  ".join(dic_mapa_comp['letra2']))  # Imprime a linha de letras



def printando_mapas (dic_mapa , dic_mapa_comp):
    pula_linha ="\n"
    print(pula_linha)
    print("           MAPA COMPUTADOR           ")   
    print(pula_linha)
    print("   " + "  ".join(dic_mapa_comp['letra']))  # Imprime a linha de letras
    for i in range(1, 11):
        linha = dic_mapa_comp[str(i)]  # Pega a linha correspondente do dicionário
        print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
    print("   " + "  ".join(dic_mapa_comp['letra2']))  # Imprime a linha de letras


    print(pula_linha)
    print(pula_linha)
    print("           MAPA JOGADOR           ")   
    print("   " + "  ".join(dic_mapa['letra']))  # Imprime a linha de letras
    for i in range(1, 11):
        linha = dic_mapa[str(i)]  # Pega a linha correspondente do dicionário
        print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
print("   " + "  ".join(dic_mapa['letra2']))  # Imprime a linha de letras


TRANSPORTE = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

import random
frota_comp = random.choice(list(PAISES.keys()))
# frota_comp = 5


lista_navios_comp2 = []

for numero, pais in PAISES.items():
    if numero==frota_comp:
        for pais,navios in pais.items():
            for navio, qntd in navios.items():
                lista_navios_comp2.extend([navio] * qntd) 
    

lista_blocos =[]
for transportes, bloco in TRANSPORTE.items():
    for aviao in lista_navios_comp2:
        if transportes == aviao:
            lista_blocos.append(bloco)
print(lista_blocos)


print(lista_navios_comp2)
                        
mapa_comp_memoria= {
    'letra': ['A','B','C','D','E','F','G','H','I','J'],
    '1': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','1'],
    '2': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','2'],
    '3': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','3'],
    '4': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','4'],
    '5': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','5'],
    '6': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','6'],
    '7': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','7'],
    '8': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','8'],
    '9': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','9'],
    '10': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','10'],
    'letra2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
}

#pegar um elemento (que representa o total de espaços que vão ser ocupados por um navio no mapa) da lista de blocos, 

for linhas, lista_espaços in mapa_comp_memoria.items():
    for a in lista_blocos:
    
        seleciona_sentido = random.choice(['h', 'v'])
        seleciona_linha = random.choice(range(1,11))
        seleciona_coluna = random.choice(range(0,10))

        if seleciona_sentido == 'v':
            while seleciona_coluna + a > len(lista_espaços)-1 :
                seleciona_linha = random.choice(range(1,11))
                seleciona_coluna = random.choice(range(0,10))
                mapa_comp_memoria[str(seleciona_linha)][seleciona_coluna]= 'N' #posicionou apenas a linha/coluna

        else:
            #sentido == h
            while seleciona_linha + a  > 10:
                # seleciona_linha = random.choice(mapa_comp_memoria.keys[1:11])
                seleciona_linha = random.choice(range(1,11))
                seleciona_coluna = random.choice(range(0,10))
                mapa_comp_memoria[str(seleciona_linha)][seleciona_coluna]= 'N'

print(seleciona_coluna)
print(seleciona_linha)
print(seleciona_sentido)


print("           MAPA MEMÓRIA     ") #Imprime nome do mapa
print("   " + "  ".join(mapa_comp_memoria['letra']))  # Imprime a linha de letras
for i in range(1, 11):
    linha = mapa_comp_memoria[str(i)]  # Pega a linha correspondente do dicionário
    print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
print("   " + "  ".join(mapa_comp_memoria['letra2']))  # Imprime a linha de letras



mapa_comp_visível= {
    'letra': ['A','B','C','D','E','F','G','H','I','J'],
    '1': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','1'],
    '2': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','2'],
    '3': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','3'],
    '4': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','4'],
    '5': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','5'],
    '6': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','6'],
    '7': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','7'],
    '8': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','8'],
    '9': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','9'],
    '10': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ','10'],
    'letra2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
}








