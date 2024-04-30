
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

lista_transporte_nome = []
numero_nacao = input('Qual o número da nação da sua frota?')

for numero in PAISES:
    if numero == numero_nacao:
        for pais, transportes_pais_qnt in numero.items():
            print ('Você escolheu a nação {0}'. format(pais))
            print ('Agora é a sua vez de alocar seus navios de guerra!')
#            print (TABULEIRO)

            for transporte_nome, quantidade in transportes_pais_qnt.items():
                lista_transporte_nome.append(transporte_nome)
                for transporte_TRANSPORTE, qnt_blocos in TRANSPORTE.items():
                    if transporte_nome == transporte_TRANSPORTE:
                        blocos = qnt_blocos 
                        print ('alocar: {0} ({1} blocos)'.format(transporte_nome, blocos))
                        for i in range(len(lista_transporte_nome)):
                            if transporte_nome != lista_transporte_nome[0]:
                                del lista_transporte_nome [i - 1]
                                resto_transporte = (' ').join(lista_transporte_nome)
                            else:   
                                resto_transporte = (' ').join(lista_transporte_nome)
                            if resto_transporte != '':
                                print ('proximos:{0}'.format(resto_transporte))
                                informe_letra = input('Informe a Letra:')
                                informe_linha = input('Informe a Linha:')
                                informe_orientacao = input ('Informe a Orientação [v|h]:')
                                print ('Navio alocado!')
                            if resto_transporte == '':
                                informe_letra = input('Informe a Letra:')
                                informe_linha = input('Informe a Linha:')
                                informe_orientacao = input ('Informe a Orientação [v|h]:')
                                print ('Todos os navios foram alocados!')
                            #PRINT TABULEIRO 

# INICIANDO BATALHA NAVAL 

print ('Iniciando a batalha naval!')
print ('5')
print ('4')
print ('3')
print ('2')
print ('1')
#intervalo tempo - fallta 



# PRINT (TABULEIRO)
# CHUTE COMPUTADOR 
#CHUTE PESSOA 
print () 

print ('Coordenadas do seu disparo')
letra = input('Letra:') 
linha = input ('Linha:') 
# ver linha 
acerto = 'Água!'or  'BOOOOOOOMMMMMM!!!!!'
print ('Jogador   ----->>>>> {0}{1}       {2}!'. fromat(letra,linha,acerto))

#Posição E6 já bombardeada!





# Você venceu!
# Temos um novo xerife nos mares!
# Jogar novamente? [s|n] 

# Você perdeu!
# Nao e bem vindo nesses mares!
# Jogar novamente? [s|n] 


































#################################################TABULEIRO################################################

Letras_maiuscula = ['A','B','C','D','E','F','G','H','I','J']
Letras_minuscula= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


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



lista_para_informe_linha =[ 1, 2, 3, 4, 5, 6, 7, ,8 ,9 ,10]

if informe_letra in Letras_minuscula or informe_letra in Letras_maiuscula:
    if informe_linha in lista_para_informe_linha:
        for numero, lista in dic_mapa.items():
            if numero == informe_linha:
                if informe_letra == 'A':
                    if [informe_linha][0] not ocupado:\
                        dic_mapa[informe_linha][0] = ™¡ª
    else: 
        print ('linha invalida')
else:
    print ('coluna invalida')
