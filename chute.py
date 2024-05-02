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
        break
    else: 
        print("Coluna inválida")
        
        
while chute_linha not in list(range(1,11)):
    chute_linha = input("Escolha uma linha (1 até 10): ")
    if chute_linha in list(range(1,11)):
        break
    else:
        print("Escolha uma linha válida")