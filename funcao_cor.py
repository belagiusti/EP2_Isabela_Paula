


def preencher_quadrado(dic_mapa, letra, numero):
    letra_index = dic_mapa['letra'].index(letra)  # Encontra o índice da letra no dicionário
    numero_index = int(numero)  # Converte o número para inteiro
    dic_mapa[str(numero_index)][letra_index] = '\033[92m█\033[0m'  # Substitui o valor na posição correspondente por 'X' verde

def imprimir_mapa(dic_mapa):
    print("   " + "  ".join(dic_mapa['letra']))  # Imprime a linha de letras

    for i in range(1, 11):
        linha = dic_mapa[str(i)]  # Pega a linha correspondente do dicionário
        print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
    print("   " + "  ".join(dic_mapa['letra2']))  # Imprime a linha de letras

# Teste de impressão do mapa após preencher o quadrado A1 com um quadrado verde
imprimir_mapa(dic_mapa)