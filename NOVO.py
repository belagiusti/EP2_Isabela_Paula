

#################################################TABULEIRO################################################

Letras_maiuscula = ['A','B','C','D','E','F','G','H','I','J']
Letras_minuscula= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numero_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for key, value in dic_mapa.items():
#     print(key)
#     for item in value:
#         print(item)
#     print()  

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

print("   " + "  ".join(dic_mapa['letra']))  # Imprime a linha de letras

for i in range(1, 11):
    linha = dic_mapa[str(i)]  # Pega a linha correspondente do dicionário
    print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
print("   " + "  ".join(dic_mapa['letra2']))  # Imprime a linha de letras


# chute jogador 
def chute_jogador (informe_letra, informe_linha, informe_orientacao):
    if informe_letra in Letras_minuscula or informe_letra in Letras_maiuscula:
        if informe_linha in numero_lista:
            for numero, lista in dic_mapa.items():
                if numero == informe_linha:
                    if informe_letra == 'A' or informe_letra == 'a':
                        if [informe_linha][0] == ' ':
                            dic_mapa[informe_linha][0] = (u"\u001b[32m   \u001b[0m")
                            print ('Navio alocado!')
                        else:
                            x = 'A' + informe_linha + informe_orientacao
                            print ('Não foi possível alocar o navio em {x}')
                    if informe_letra == 'B' or informe_letra == 'b':
                        if [informe_linha][1] == ' ':
                            dic_mapa[informe_linha][1] = (u"\u001b[32m   \u001b[0m")
                            print ('Navio alocado!')
                        else:
                            x = 'B' + informe_linha + informe_orientacao
                            print ('Não foi possível alocar o navio em {x}')
                    if informe_letra == 'C' or informe_letra == 'c':
                        if [informe_linha][2] == ' ':
                            dic_mapa[informe_linha][2] = (u"\u001b[32m   \u001b[0m")
                            print ('Navio alocado!')
                        else:
                            x = 'C' + informe_linha + informe_orientacao
                            print ('Não foi possível alocar o navio em {x}')
                    if informe_letra == 'D' or informe_letra == 'd':
                        if [informe_linha][3] == ' ':
                            dic_mapa[informe_linha][3] = (u"\u001b[32m   \u001b[0m")
                            print ('Navio alocado!')
                        else:
                            x = 'D' + informe_linha + informe_orientacao
                            print ('Não foi possível alocar o navio em {x}')
                    if informe_letra == 'E' or informe_letra == 'e':
                        if [informe_linha][4] == ' ':
                            dic_mapa[informe_linha][4] = (u"\u001b[32m   \u001b[0m")
                            print ('Navio alocado!')
                        else:
                            x = 'E' + informe_linha + informe_orientacao
                            print ('Não foi possível alocar o navio em {x}')
                    if informe_letra == 'F' or informe_letra == 'f':
                        if [informe_linha][5] == ' ':
                            dic_mapa[informe_linha][5] = (u"\u001b[32m   \u001b[0m")
                            print ('Navio alocado!')
                        else:
                            x = 'F' + informe_linha + informe_orientacao
                            print ('Não foi possível alocar o navio em {x}')
                    if informe_letra == 'G' or informe_letra == 'g':
                        if [informe_linha][6] == ' ':
                            dic_mapa[informe_linha][6] = (u"\u001b[32m   \u001b[0m")
                            print ('Navio alocado!')
                        else:
                            x = 'G' + informe_linha + informe_orientacao
                            print ('Não foi possível alocar o navio em {x}')
                    if informe_letra == 'H' or informe_letra == 'h':
                        if [informe_linha][7] == ' ':
                            dic_mapa[informe_linha][7] = (u"\u001b[32m   \u001b[0m")
                            print ('Navio alocado!')
                        else:
                            x = 'H' + informe_linha + informe_orientacao
                            print ('Não foi possível alocar o navio em {x}')
                    if informe_letra == 'I' or informe_letra == 'i':
                        if [informe_linha][8] == ' ':
                            dic_mapa[informe_linha][8] = (u"\u001b[32m   \u001b[0m")
                            print ('Navio alocado!')
                        else:
                            x = 'I' + informe_linha + informe_orientacao
                            print ('Não foi possível alocar o navio em {x}')
                    if informe_letra == 'J' or informe_letra == 'j':
                        if [informe_linha][9] == ' ':
                            dic_mapa[informe_linha][9] = (u"\u001b[32m   \u001b[0m")
                            print ('Navio alocado!')
                        else:
                            x = 'J' + informe_linha + informe_orientacao
                            print ('Não foi possível alocar o navio em {x}')
        else: 
            y = 'linha invalida'
            print (y)
    else:
        y = 'coluna invalida'
        print (y)


 #   if y == 'coluna invalida' or y == 'linha invalida':
        

















































##############################################################################################

TRANSPORTE = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

# frotas de cada pais
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

print (PAISES)
# print paises certo 



numero_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_nacao = int(input('Qual o número da nação da sua frota?'))
QUANT_T  = 0  
lista_transporte_nome = []     
for i in range(len(numero_lista)):
    if numero_lista[i] == numero_nacao:
        for pais, dic_transportes in PAISES[numero_lista[i]].items():
            print('Você escolheu a nação {0}'.format(pais))
            print('Agora é a sua vez de alocar seus navios de guerra!')
            # print tabuleiro 
    
            for transporte_nome, quantidade in dic_transportes.items():
                lista_transporte_nome.extend([transporte_nome] * quantidade)
                
                QUANT_T += quantidade
aloca = lista_transporte_nome[0]
del lista_transporte_nome [0]
for transporte_nome, quantidade in TRANSPORTE.items():
    if transporte_nome == aloca:
        for i in range(0,QUANT_T):
            if lista_transporte_nome== []:
                print('Alocar: {0} ({1} blocos)'.format(aloca, quantidade))
                informe_letra = input('Informe a Letra:')
                informe_linha = input('Informe a Linha:')
                informe_orientacao = input ('Informe a Orientação [v|h]:')
                chute_jogador (informe_letra, informe_linha, informe_orientacao)
                print ('Todos os navios foram alocados!')
                #print tabuleiro final alocado 
                print ('Iniciando a batalha naval!')
                print ('5')
                print ('4')
                print ('3')
                print ('2')
                print ('1')
                #intervalo tempo - fallta 
                # INICIO BATALHA NAVAL 
            else: 
                print('Alocar: {0} ({1} blocos)'.format(aloca, quantidade))
                print('Próximos: {0}'.format(', '.join(lista_transporte_nome)))
                aloca = lista_transporte_nome[0]
                del lista_transporte_nome [0]
                informe_letra = input('Informe a Letra:')
                informe_linha = input('Informe a Linha:')
                informe_orientacao = input ('Informe a Orientação [v|h]:')
                 # ver se pode alocar - chamar funcao - nao colocar codigo aqui 
                 # se nao pode alocar: print()'Não foi possível alocar o navio em A1 h(informe_letra+ informe_linha + informe_orientacao)
                chute_jogador (informe_letra, informe_linha, informe_orientacao)
                #print tabuleiro com navio alocado - chamar funcao apenas 

            
            # pintar tabuleiro e printar 



# CHUTE COMPUTADOR 
#CHUTE PESSOA 
print () 

print ('Coordenadas do seu disparo')
informe_letra = input('Letra:') 
informe_linha = input ('Linha:') 

# # ver linha 
# acerto = 'Água!'or  'BOOOOOOOMMMMMM!!!!!'
# print ('Jogador   ----->>>>> {0}{1}       {2}!'. format(informe_letra,informe_linha,acerto))

# #Posição E6 já bombardeada!





# Você venceu!
# Temos um novo xerife nos mares!
# Jogar novamente? [s|n] 

# Você perdeu!
# Nao e bem vindo nesses mares!
# Jogar novamente? [s|n] 











