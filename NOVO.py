import random 

#################################################TABULEIRO JOGADOR################################################
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

def mapa_vazio (dic_mapa):
    print("   " + "  ".join(dic_mapa['letra']))  # Imprime a linha de letras

    for i in range(1, 11):
        linha = dic_mapa[str(i)]  # Pega a linha correspondente do dicionário
        print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
    print("   " + "  ".join(dic_mapa['letra2']))  # Imprime a linha de letras




#ALGUMAS LISTAS
Letras_maiuscula = ['A','B','C','D','E','F','G','H','I','J']
Letras_minuscula= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numero_lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
vh_lista = ['v', 'h']




################################ O COMECO!
nacao_computador =  random.choice(['Brasil', 'França','Austrália','Rússia','Japão'])

print (' =====================================')
print ('|                                     |')
print ('| Bem-vindo ao INSPER - Batalha Naval |')
print ('|                                     |')
print (' =======   xxxxxxxxxxxxxxxxx   ======= ')
print ('')
print ('')
print ('Iniciando o Jogo!')
print ('Computador está alocando os navios de guerra do país {0}...'. format(nacao_computador))
print('Computador já está em posição de batalha!')
print ('')















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


import math
import random
pula_linha =  '\n'
texto = '1 = Brasil:'+ pula_linha + 'cruzador: 1' + pula_linha + 'torpedeiro: 2'+ pula_linha+  'destroyer: 1' + pula_linha + 'couracado: 1' + pula_linha +'porta-avioes: 1'+ pula_linha +  pula_linha + '2 = França:'+pula_linha +'cruzador: 3' + pula_linha +'porta-avioes: 1'+ pula_linha+'destroyer: 1'+pula_linha+'submarino: 1' +pula_linha+'couracado: 1'+pula_linha+pula_linha + '3 = Austrália:' + pula_linha + 'couracado: 1'+ pula_linha +'cruzador: 3' +pula_linha+ 'submarino: 1'+pula_linha+ 'porta-avioes: 1'+pula_linha+'torpedeiro: 1'+pula_linha+pula_linha+'4 = Rússia:'+pula_linha+'cruzador: 1'+pula_linha+'porta-avioes: 1'+pula_linha +'couracado: 2'+pula_linha+'destroyer: 1'+pula_linha+'submarino: 1'+pula_linha+pula_linha+'5 = Japão:'+pula_linha+ 'torpedeiro: 2'+pula_linha+'cruzador: 1'+pula_linha+'destroyer: 2'+pula_linha+'couracado: 1'+pula_linha+'submarino: 1'+pula_linha
print(texto)
# COMECO - PRINT LISTA PAISES E TROPAS 




# LISTA DE TRANSPORTES PARA PRINTAR PARA JOGADOR 
numero_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_nacao = int(input('Qual o número da nação da sua frota?'))
QUANT_T  = 0  
lista_transporte_nome = []     
for i in range(len(numero_lista)):
    if numero_lista[i] == numero_nacao:
        for pais, dic_transportes in PAISES[numero_lista[i]].items():
            print ('')
            print('Você escolheu a nação {0}'.format(pais))
            print('Agora é a sua vez de alocar seus navios de guerra!')
            print ('')
            mapa_vazio (dic_mapa) ## printar do compr - arrumar 
            print ('')
            # print tabuleiroS
    
            for transporte_nome, quantidade in dic_transportes.items():
                lista_transporte_nome.extend([transporte_nome] * quantidade)
                
                QUANT_T += quantidade



LISTA_TRANSPORTE_NOME_SEM_ALTERACAO =  lista_transporte_nome    ## PARA JOGADOR_ALOCA - DEIXAR AQUI MESMO           
aloca = lista_transporte_nome[0]
del lista_transporte_nome [0]




numero_lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
vh_lista = ['v', 'h']



# COMECO JOGO E PERGUNTAS PARA ALOCAR 
for transporte_nome, quantidade in TRANSPORTE.items():
    if transporte_nome == aloca:
        for i in range(0,QUANT_T):
            if lista_transporte_nome== []:
                print('Alocar: {0} ({1} blocos)'.format(aloca, quantidade))
                informe_letra = input('Informe a Letra:')
                informe_linha = input('Informe a Linha:')
                informe_orientacao = input ('Informe a Orientação [v|h]:')
                aloca_jogador (informe_letra, informe_linha, informe_orientacao,quantidade) # so esta colorindo a letra e numero citado, falta adcionar qnt de blocos e direcao
                print('Todos os navios foram alocados!')
                # #print tabuleiro final alocado 
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
                aloca_jogador(informe_letra, informe_linha, informe_orientacao,quantidade)
                #print tabuleiro com navio alocado - chamar funcao apenas 

            
            # pintar tabuleiro e printar 







######## COMECO DO JOGO E CHUTES!!!!!!!!!###########



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
# O computador ainda é o senhor dos mares!
# Jogar novamente? [s|n] 








