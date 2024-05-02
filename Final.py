import constantes
import math
import random
from constantes import*
pula_linha =  '\n'
texto = '1 = Brasil:'+ pula_linha + 'cruzador: 1' + pula_linha + 'torpedeiro: 2'+ pula_linha+  'destroyer: 1' + pula_linha + 'couracado: 1' + pula_linha +'porta-avioes: 1'+ pula_linha +  pula_linha + '2 = França:'+pula_linha +'cruzador: 3' + pula_linha +'porta-avioes: 1'+ pula_linha+'destroyer: 1'+pula_linha+'submarino: 1' +pula_linha+'couracado: 1'+pula_linha+pula_linha + '3 = Austrália:' + pula_linha + 'couracado: 1'+ pula_linha +'cruzador: 3' +pula_linha+ 'submarino: 1'+pula_linha+ 'porta-avioes: 1'+pula_linha+'torpedeiro: 1'+pula_linha+pula_linha+'4 = Rússia:'+pula_linha+'cruzador: 1'+pula_linha+'porta-avioes: 1'+pula_linha +'couracado: 2'+pula_linha+'destroyer: 1'+pula_linha+'submarino: 1'+pula_linha+pula_linha+'5= Japão:'+pula_linha+ 'torpedeiro: 2'+pula_linha+'cruzador: 1'+pula_linha+'destroyer: 2'+pula_linha+'couracado: 1'+pula_linha+'submarino: 1'+pula_linha
print(texto)

##########################################################################################
from Tabuleiro_Comp import*

# print("           MAPA MEMÓRIA     ") #Imprime nome do mapa
# print("   " + "  ".join(mapa_comp_memoria['letra']))  # Imprime a linha de letras
# for i in range(1, 11):
#     linha = mapa_comp_memoria[str(i)]  # Pega a linha correspondente do dicionário
#     print(str(i).rjust(2) + " " + "  ".join(linha))  # Imprime a linha com o número à esquerda e os valores separados por espaço
# print("   " + "  ".join(mapa_comp_memoria['letra2']))  # Imprime a linha de letras



print (' =====================================')
print ('|                                     |')
print ('| Bem-vindo ao INSPER - Batalha Naval |')
print ('|                                     |')
print (' =======   xxxxxxxxxxxxxxxxx   ======= ')
print ('')
print ('')
print ('Iniciando o Jogo!')
print ('Computador está alocando os navios de guerra do país {0}...'. format(frota_comp))
print('Computador já está em posição de batalha!')
print ('')

#ALOCA NAVIO DO JOGADOR

from chute import* # COLOCAR EM LOOP

#CRIAR ATAQUE ALEATÓRIO DO COMP NO TAB JOGADOR # COLOCAR EM LOOP




# Você venceu!
# Temos um novo xerife nos mares!
# Jogar novamente? [s|n] 

# Você perdeu!
# O computador ainda é o senhor dos mares!
# Jogar novamente? [s|n] 

