
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
for a in lista_blocos:
    seleciona_sentido = random.choice(['h', 'v'])
    seleciona_linha = 100
    seleciona_coluna = 100

    if seleciona_sentido == 'v':
        for linhas, lista_espaços in mapa_comp_memoria.items():
            while seleciona_coluna + a > len(lista_espaços)-1 :
                seleciona_linha = random.choice(range(1,11))
                seleciona_coluna = random.choice(range(0,10))
            
            if mapa_comp_memoria[str(seleciona_linha)][seleciona_coluna]== " " : 
                mapa_comp_memoria[str(seleciona_linha)][seleciona_coluna]= 'N' #posicionou apenas a linha/coluna
                #enquanto os espaços coluna+blocos != "N"
                for n in list(range(0, a)):
                    while mapa_comp_memoria[str(seleciona_linha)][seleciona_coluna+n] != "N":
                        mapa_comp_memoria[str(seleciona_linha)][seleciona_coluna+n] = "N"

                    
                #mapa_comp_memoria[str(seleciona_linha)][seleciona_coluna+(a)] 

    else:#sentido == h
        for linhas, lista_espaços in mapa_comp_memoria.items():    
            while seleciona_linha + a  > 10:
                seleciona_linha = random.choice(range(1,11))
                seleciona_coluna = random.choice(range(0,10))

            if mapa_comp_memoria[str(seleciona_linha)][seleciona_coluna]== " ": 
                mapa_comp_memoria[str(seleciona_linha)][seleciona_coluna]= 'N'
                for n in list(range(1, a+1)):
                    while mapa_comp_memoria[str(seleciona_linha+n)][seleciona_coluna] != "N":
                        mapa_comp_memoria[str(seleciona_linha+n)][seleciona_coluna] = "N"




# print("           MAPA MEMÓRIA     ") #Imprime nome do mapa
# print("   " + "  ".join(mapa_comp_memoria['letra']))  # Imprime a linha de letras
# for i in range(1, 11):
#     linha = mapa_comp_memoria[str(i)]  # Pega a linha correspondente do dicionário
#     print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
# print("   " + "  ".join(mapa_comp_memoria['letra2']))  # Imprime a linha de letras












