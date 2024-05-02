from Tabuleiro_Comp import *
print("Sua vez de ATACAR!")
chute_letra =''
chute_linha =''
letr =['A','B','C','D','E','F','G','H','I','J']
letrinha=['a','b','c','d','e','f','g','h','i','j']
letr =['A','B','C','D','E','F','G','H','I','J']
letrinha=['a','b','c','d','e','f','g','h','i','j']
while chute_letra not in letr or chute_letra not in letrinha:
    chute_letra = input("Escolha uma Coluna (A até J): ")
    if chute_letra in letr or chute_letra in letrinha:
        if chute_letra in letr:
            posicao = letr.index(chute_letra)
        else:
            posicao = letrinha.index(chute_letra) 
        break
    else: 
        print("Coluna inválida")

        

        
print (list(range(1,11)) ) 

l_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while chute_linha not in l_num:
    chute_linha = int(input("Escolha uma linha (1 até 10): "))
    print(chute_linha)
    if chute_linha in l_num:
        break
    else:
        print("Selecione uma linha válida")


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

#Checa se a pessoa acertou o chute
if  mapa_comp_memoria[str(seleciona_linha)][seleciona_coluna]== " ": 
    mapa_comp_visível[str(chute_linha )][(posicao)]= "E" #marca bloco

elif mapa_comp_memoria[str(seleciona_linha)][seleciona_coluna]== "N": 
    mapa_comp_visível[str(chute_linha )][(posicao)]= 'A'

elif mapa_comp_visível[str(chute_linha )][(posicao)]== 'A' or mapa_comp_visível[str(chute_linha )][(posicao)]== "E": 
    print("Esse espaço já foi chutado anteriormente")


print("           MAPA COMPUTADOR    ") #Imprime nome do mapa
print("   " + "  ".join(mapa_comp_visível['letra']))  # Imprime a linha de letras
for i in range(1, 11):
    linha = mapa_comp_visível[str(i)]  # Pega a linha correspondente do dicionário
    print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
print("   " + "  ".join(mapa_comp_visível['letra2']))  # Imprime a linha de letras
