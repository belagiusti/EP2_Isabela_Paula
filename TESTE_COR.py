# def quadrado_verde():
#     tamanho = 5  # Tamanho do lado do quadrado
#     texto = "  "  # Texto vazio

#     # Define a cor verde ANSI
#     cor_verde = "\033[92m"

#     # Define o caractere de preenchimento para o quadrado
#     caractere_preenchimento = "#"

#     # Gera o quadrado com o texto vazio
#     quadrado = [[texto for _ in range(tamanho)] for _ in range(tamanho)]

#     # Preenche o quadrado com a cor verde e o caractere de preenchimento
#     for i in range(tamanho):
#         for j in range(tamanho):
#             quadrado[i][j] = cor_verde + caractere_preenchimento + "\033[0m"

#     # Retorna o quadrado como uma string
#     return '\n'.join([' '.join(fila) for fila in quadrado])

# # Chama a função e imprime o quadrado verde
# print(quadrado_verde())







# def quadrado_verde():
#     tamanho = 4  # Tamanho do lado do quadrado

#     # Define a cor verde ANSI
#     cor_verde = "\033[92m"
    
#     # Define o caractere de preenchimento para o quadrado
#     caractere_preenchimento = "█"

#     # Gera o quadrado com espaços em branco
#     quadrado = [[caractere_preenchimento for _ in range(tamanho)] for _ in range(tamanho)]

#     # Preenche todo o quadrado com a cor verde
#     for i in range(tamanho):
#         for j in range(tamanho):
#             quadrado[i][j] = cor_verde + caractere_preenchimento + "\033[0m"

#     # Retorna o quadrado como uma string
#     return '\n'.join([' '.join(fila) for fila in quadrado])

# # Chama a função e imprime o quadrado verde
# print(quadrado_verde())







# def quadrado_verde():
#     tamanho = 10  # Tamanho do tabuleiro
#     largura_borda = 1  # Largura da borda entre os quadrados

#     # Define a cor verde ANSI
#     cor_verde = "\033[92m"
#     # Define a cor azul ANSI
#     cor_azul = "\033[94m"
    
#     # Define o caractere de preenchimento para o quadrado
#     caractere_preenchimento = "█"
#     caractere_agua = "~"

#     # Inicializa a string de resultado
#     resultado = ""

#     # Loop para preencher o tabuleiro com quadrados verdes
#     for i in range(tamanho):
#         for j in range(tamanho):
#             # Verifica se está em uma célula de água
#             if (i + j) % 2 == 0:
#                 # Adiciona a cor azul e o caractere de água para as células de água
#                 resultado += cor_azul + caractere_agua
#             else:
#                 # Adiciona a cor verde e o caractere de preenchimento para as células de terra
#                 resultado += cor_verde + caractere_preenchimento
#         resultado += "\n"  # Adiciona uma quebra de linha no final de cada linha
#     return resultado

# # Chama a função e imprime o resultado
# print(quadrado_verde())









def preencher_quadrado(dic_mapa, letra, numero):
    letra_index = dic_mapa['letra'].index(letra)  # Encontra o índice da letra no dicionário
    numero_index = int(numero)  # Converte o número para inteiro
    dic_mapa[str(numero_index)][letra_index] = '\033[92m█\033[0m'  # Substitui o valor na posição correspondente por 'X' verde

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

# Teste da função
preencher_quadrado(dic_mapa, 'A', '1')

# Função para imprimir o mapa
def imprimir_mapa(dic_mapa):
    print("   " + "  ".join(dic_mapa['letra']))  # Imprime a linha de letras

    for i in range(1, 11):
        linha = dic_mapa[str(i)]  # Pega a linha correspondente do dicionário
        print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
    print("   " + "  ".join(dic_mapa['letra2']))  # Imprime a linha de letras

# Teste de impressão do mapa após preencher o quadrado A1 com um quadrado verde
imprimir_mapa(dic_mapa)