from Tabuleiro_Comp import*
import time
import random
c = 0 
def FUNCAO_JOGO_FINAL(c):
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
    # nacao_computador = random.choice(['Brasil', 'França', 'Austrália', 'Rússia', 'Japão'])

    if frota_comp == 1:
        nacao_computador = 'Brasil'
    if frota_comp == 2:
        nacao_computador = 'França'
    if frota_comp == 1:
        nacao_computador = 'Austrália'
    if frota_comp == 1:
        nacao_computador = 'Rússia'
    if frota_comp == 1:  
        nacao_computador = 'Japão'



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


    print("Sua vez de ATACAR!")
    pontos_jogador = 0 
    pontos_computador = 0

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


    print("           MAPA COMPUTADOR         ") #Imprime nome do mapa
    print("   " + "  ".join(mapa_comp_visível['letra']))  # Imprime a linha de letras
    for i in range(1, 11):
        linha = mapa_comp_visível[str(i)]  # Pega a linha correspondente do dicionário
        print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
    print("   " + "  ".join(mapa_comp_visível['letra2']))  # Imprime a linha de letras

    chute_letra =''
    chute_linha =''
    letr =['A','B','C','D','E','F','G','H','I','J']
    letrinha=['a','b','c','d','e','f','g','h','i','j']


    while pontos_jogador<20 or pontos_computador <20:
        print("Sua vez de ATACAR!")

        chute_letra = input("Escolha uma Coluna (A até J): ")
        while chute_letra not in letr and chute_letra not in letrinha:
            print("Coluna inválida")
            chute_letra = input("Escolha uma Coluna (A até J): ")
        if chute_letra in letr:
            posicao = letr.index(chute_letra)
        else:                    
            posicao = letrinha.index(chute_letra)


        l_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        chute_linha=0
        while chute_linha not in l_num :
            chute_linha = int(input("Escolha uma linha (1 até 10): "))
            if chute_linha not in l_num:
                print("Selecione uma linha válida")

        #Checa se a pessoa acertou o chute
        if mapa_comp_memoria[str(chute_linha )][posicao]== "N": 
            mapa_comp_visível[str(chute_linha )][(posicao)]= '\033[91m∎\033[0m' 
            print("BOOOOOM! Você acertou")
            pontos_jogador+=1
        elif  mapa_comp_memoria[str(chute_linha)][posicao]== " ": 
            mapa_comp_visível[str(chute_linha )][(posicao)]=  '\033[34m∎\033[0m' 
            print("Você Errou")

        elif mapa_comp_visível[str(chute_linha )][(posicao)]== '\033[91m∎\033[0m' or mapa_comp_visível[str(chute_linha )][(posicao)]== '\033[34m∎\033[0m': 
            print("Esse espaço já foi chutado anteriormente")



        print("           MAPA COMPUTADOR         ") #Imprime nome do mapa
        print("   " + "  ".join(mapa_comp_visível['letra']))  # Imprime a linha de letras
        for i in range(1, 11):
            linha = mapa_comp_visível[str(i)]  # Pega a linha correspondente do dicionário
            print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
        print("   " + "  ".join(mapa_comp_visível['letra2']))  # Imprime a linha de letras

        #CHUTE COMP NO JOG
        linha_chute = random.choice(range(1,10))
        coluna_chute = random.choice(range(0,9))
        for linha, lista_situacao in dic_mapa.items():
            if dic_mapa[str(linha_chute)][coluna_chute] == '\033[95m∎\033[0m':  
                dic_mapa[str(linha_chute)][coluna_chute] = '\033[91m∎\033[0m'
                print("Você foi atacado!")
                pontos_computador+=1
            elif dic_mapa[str(linha_chute)][coluna_chute] == ' ': 
                dic_mapa[str(linha_chute)][coluna_chute] = '\033[34m∎\033[0m'
                


        print("           MAPA JOGADOR       ") #Imprime nome do mapa
        print("   " + "  ".join(dic_mapa['letra']))  # Imprime a linha de letras
        for i in range(1, 11):
            linha = dic_mapa[str(i)]  # Pega a linha correspondente do dicionário
            print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
        print("   " + "  ".join(dic_mapa['letra2']))  # Imprime a linha de letras


    if pontos_computador>pontos_jogador:
        return (print("Você perdeu"))
    else:
        return (print("Você ganhou!"))
    
    
print(FUNCAO_JOGO_FINAL(c)    )

jogar_novamente = input("Jogar novamente? [s|n]")
if jogar_novamente == 's':
    FUNCAO_JOGO_FINAL(c)
if jogar_novamente == 'n':
    print ('Até a próxima!')


