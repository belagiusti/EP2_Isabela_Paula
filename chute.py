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
        
print (list(range(1,11)) ) 

l_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while chute_linha not in l_num:
    chute_linha = int(input("Escolha uma linha (1 até 10): "))
    print(chute_linha)
    if chute_linha in l_num:
        break
    else:
        print("Selecione uma linha válida")
    
