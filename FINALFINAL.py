import time
import random

dic_mapa = {
    'letra': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    '1': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
    '2': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2'],
    '3': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '3'],
    '4': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '4'],
    '5': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '5'],
    '6': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '6'],
    '7': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '7'],
    '8': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8'],
    '9': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '9'],
    '10': [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '10'],
    'letra2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
}

def mapa_vazio(dic_mapa):
    print ('         TABULEIRO JOGADOR        ')
    print("   " + "  ".join(dic_mapa['letra']))  # Imprime a linha de letras

    for i in range(1, 11):
        linha = dic_mapa[str(i)]  # Pega a linha correspondente do dicionário
        print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
    print("   " + "  ".join(dic_mapa['letra2']))  # Imprime a linha de letras

#ALGUMAS LISTAS
letras_validas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numeros_validos = range(1, 11)
vh_lista = ['v', 'h']

################################ O COMECO!
nacao_computador = random.choice(['Brasil', 'França', 'Austrália', 'Rússia', 'Japão'])

print(' =====================================')
print('|                                     |')
print('| Bem-vindo ao INSPER - Batalha Naval |')
print('|                                     |')
print(' =======   xxxxxxxxxxxxxxxxx   ======= ')
print('')
print('')
print('Iniciando o Jogo!')
print('Computador está alocando os navios de guerra do país {0}...'.format(nacao_computador))
print('Computador já está em posição de batalha!')
print('')
pula_linha =  '\n'
texto = '1 = Brasil:'+ pula_linha + 'cruzador: 1' + pula_linha + 'torpedeiro: 2'+ pula_linha+  'destroyer: 1' + pula_linha + 'couracado: 1' + pula_linha +'porta-avioes: 1'+ pula_linha +  pula_linha + '2 = França:'+pula_linha +'cruzador: 3' + pula_linha +'porta-avioes: 1'+ pula_linha+'destroyer: 1'+pula_linha+'submarino: 1' +pula_linha+'couracado: 1'+pula_linha+pula_linha + '3 = Austrália:' + pula_linha + 'couracado: 1'+ pula_linha +'cruzador: 3' +pula_linha+ 'submarino: 1'+pula_linha+ 'porta-avioes: 1'+pula_linha+'torpedeiro: 1'+pula_linha+pula_linha+'4 = Rússia:'+pula_linha+'cruzador: 1'+pula_linha+'porta-avioes: 1'+pula_linha +'couracado: 2'+pula_linha+'destroyer: 1'+pula_linha+'submarino: 1'+pula_linha+pula_linha+'5= Japão:'+pula_linha+ 'torpedeiro: 2'+pula_linha+'cruzador: 1'+pula_linha+'destroyer: 2'+pula_linha+'couracado: 1'+pula_linha+'submarino: 1'+pula_linha
print(texto)

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
PAISES = {
    1: {
        'Brasil': {
            'cruzador': 1,
            'torpedeiro': 2,
            'destroyer': 1,
            'couracado': 1,
            'porta-avioes': 1
        }
    },
    2: {
        'França': {
            'cruzador': 3,
            'porta-avioes': 1,
            'destroyer': 1,
            'submarino': 1,
            'couracado': 1
        }
    },
    3: {
        'Austrália': {
            'couracado': 1,
            'cruzador': 3,
            'submarino': 1,
            'porta-avioes': 1,
            'torpedeiro': 1
        }
    },
    4: {
        'Rússia': {
            'cruzador': 1,
            'porta-avioes': 1,
            'couracado': 2,
            'destroyer': 1,
            'submarino': 1
        }
    },
    5: {
        'Japão': {
            'torpedeiro': 2,
            'cruzador': 1,
            'destroyer': 2,
            'couracado': 1,
            'submarino': 1
        }
    }
}
def aloca_jogador(informe_letra, informe_linha, informe_orientacao, blocos):
    letras_validas = ['A','B','C','D','E','F','G','H','I','J']
    numeros_validos = range(1, 11)
    orientacoes_validas = ['v', 'h']

    informe_letra = informe_letra.upper()  # Convertendo a letra para maiúscula
    if informe_letra not in letras_validas:
        print("Entrada inválida! Por favor, insira uma letra de A a J.")
        return
    
    try:
        linha = int(informe_linha)  # Convertendo o número da linha para inteiro
        if linha not in numeros_validos:
            raise ValueError
    except ValueError:
        print("Entrada inválida! Por favor, insira um número de linha válido (1 a 10).")
        return
    
    coluna = letras_validas.index(informe_letra)  # Convertendo a letra para índice (0 a 9)

    # Verificando se a alocação é possível
    if informe_orientacao.lower() == 'h':
        if coluna + blocos > 10:  # Coluna + quantidade deve ser menor ou igual a 10
            print("Não é possível alocar o navio nessa posição e orientação.")
            return
        for c in range(coluna, coluna + blocos):
            if dic_mapa[str(linha)][c] != ' ':
                print("Não é possível alocar o navio nessa posição e orientação.")
                return
        # Alocando o navio
        for c in range(coluna, coluna + blocos):
            dic_mapa[str(linha)][c] = '\033[95m∎\033[0m'  # Define a cor roxa para o caractere ▒
    else:
        if linha + blocos > 10:  # Linha + quantidade deve ser menor ou igual a 10
            print("Não é possível alocar o navio nessa posição e orientação.")
            return
        for l in range(linha, linha + blocos):
            if dic_mapa[str(l)][coluna] != ' ':
                print("Não é possível alocar o navio nessa posição e orientação.")
                return
        # Alocando o navio
        for l in range(linha, linha + blocos):
            dic_mapa[str(l)][coluna] = '\033[95m∎\033[0m'  # Define a cor roxa para o caractere ▒

    # Mostrando o tabuleiro atualizado
    mapa_vazio(dic_mapa)

# Função para imprimir o tabuleiro
def print_tabuleiro(tabuleiro):
    letras = "  A B C D E F G H I J"
    print(letras)
    for i in range(10):
        print(str(i + 1) + ' ' + ' '.join(tabuleiro[i]))


# Inicializando o tabuleiro vazio
tabuleiro = [[' ']*10 for _ in range(10)]

# Aqui continua o seu código existente...

# Aqui continua o seu código existente...

# Função para imprimir o tabuleiro
def print_tabuleiro(tabuleiro):
    letras = "  A B C D E F G H I J"
    print(letras)
    for i in range(10):
        print(str(i + 1) + ' ' + ' '.join(tabuleiro[i]))

# Inicializando o tabuleiro vazio
tabuleiro = [[' ']*10 for _ in range(10)]

# Aqui continua o seu código existente...

# Definição da lista numero_lista
numero_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função para alocar os navios do jogador


def aloca_navios_jogador():
    QUANT_T = 0
    # Pergunta sobre a nação
    numero_nacao = input('Qual o número da nação da sua frota? ')
    if int(numero_nacao) in PAISES:
        for pais, dic_transportes in PAISES[int(numero_nacao)].items():
            print('')
            print('Você escolheu a nação {0}'.format(pais))
            print('Agora é a sua vez de alocar seus navios de guerra!')
            print('')
            mapa_vazio(dic_mapa)  # Imprime o tabuleiro vazio
            print('')
            # Adiciona os nomes dos transportes à lista
            lista_transporte_nome = []
            for transporte_nome, quantidade in dic_transportes.items():
                lista_transporte_nome.extend([transporte_nome] * quantidade)
                QUANT_T += quantidade


        # Loop para alocar os navios do jogador
        # for transporte_nome, blocos in TRANSPORTE.items():
        #     if transporte_nome == aloca:
        for i in range(len(lista_transporte_nome)):
                aloca = lista_transporte_nome[i]
                if aloca == 'destroyer':
                    blocos = 3
                if aloca == 'porta-avioes':
                    blocos = 5
                if aloca == 'submarino': 
                    blocos = 2
                if aloca == 'torpedeiro': 
                    blocos = 3
                if aloca == 'cruzador':
                    blocos =  2
                if aloca == 'couracado': 
                    blocos = 4
                print(f'Alocar: {aloca} ({blocos})')
                print(f'Próximos: {lista_transporte_nome[i+1:]}')
                informe_letra = input('Informe a Letra:')
                informe_linha = input('Informe a Linha:')
                informe_orientacao = input('Informe a Orientação [v|h]:')
                aloca_jogador(informe_letra, informe_linha, informe_orientacao, blocos)
                # Remove o transporte alocado da lista

        print('Todos os navios foram alocados!')
        mapa_vazio(dic_mapa)
        print('Iniciando a batalha naval!')
        for e in list(range(5,0,-1)):
            print (e)
            time.sleep(1)
        # Adicione aqui o código para iniciar a batalha naval

    else:
        print("Nação não encontrada!")

# Chamada da função para alocar os navios do jogador
aloca_navios_jogador()









## NAVIOS JOGADOR ALOCADO !!!!!!!!!!!!!!!!!!!





mapa_vazio(dic_mapa)
#MAPA COMP PRINTAR 





# COMECAR CHUTES - NAO MISTURAR COM A PARTE DE CIMA - ISSO E OUTRA PARTE DO JOGO
# COLOCAR CHUTE COMP E CHUTE JOG 
# SEMPRE PRINTANDO SEUS MAPAS!
