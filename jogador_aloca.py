import NOVO.py


# chute jogador 

def aloca_jogador (informe_letra, informe_linha, informe_orientacao,quantidade):

    T = 0 
    while T < len(LISTA_TRANSPORTE_NOME_SEM_ALTERACAO):
        

        # perguntar denovo
        if y == 'Orientação inválida' or y == 'coluna invalida' or y == 'linha invalida' or y == 'Não foi possível alocar o navio':
            informe_letra = input('Informe a Letra:')
            informe_linha = input('Informe a Linha:')
            informe_orientacao = input ('Informe a Orientação [v|h]:')
        


        #alocar/verifica 
        if informe_letra in Letras_minuscula or informe_letra in Letras_maiuscula:
            if informe_linha in numero_lista:
                if informe_orientacao in vh_lista:
                    for numero, lista in dic_mapa.items():
                        if numero == informe_linha:



                            # LETRA A 
                            if informe_letra == 'A' or informe_letra == 'a':
                                if informe_orientacao == 'h':
                                    #verificar se cabe o navio com a qnt de blocos 
                                    c = 0 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade-1:
                                        if dic_mapa[informe_linha][c] == ' ':
                                            qnt_verifica_h += 1 
                                            c += 1
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 0 
                                                while c2 <= quantidade-1:
                                                    dic_mapa[informe_linha][c2] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
                                                T += 1 # conta quantas vezes ja pergntou e deu certo

                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)
  #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A h 
                                if informe_orientacao == 'v':
                                    c = 0 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade-1:
                                        if dic_mapa[informe_linha+c][0] == ' ':
                                            qnt_verifica_h += 1 
                                            c += 1 
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 0 
                                                while c2 <= quantidade-1:
                                                    dic_mapa[informe_linha+c2][0] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
   #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A v
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)  







                             # LETRA B
                            if informe_letra == 'B' or informe_letra == 'b':
                                if informe_orientacao == 'h':
                                    #verificar se cabe o navio com a qnt de blocos 
                                    c = 1 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade:
                                        if dic_mapa[informe_linha][c] == ' ':
                                            qnt_verifica_h += 1 
                                            c += 1
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 1
                                                while c2 <= quantidade:
                                                    dic_mapa[informe_linha][c2] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
                                                T += 1 # conta quantas vezes ja pergntou e deu certo
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)
  #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A h 
                                if informe_orientacao == 'v':
                                    c = 0 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade-1:
                                        if dic_mapa[informe_linha+c][1] == ' ':
                                            qnt_verifica_h += 1
                                            c += 1 
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 0
                                                while c2 <= quantidade-1:
                                                    dic_mapa[informe_linha+c2][1] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
   #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A v
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)  




                
                        
                            
                             # LETRA C
                            if informe_letra == 'C' or informe_letra == 'c':
                                if informe_orientacao == 'h':
                                    #verificar se cabe o navio com a qnt de blocos 
                                    c = 2 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade+2:
                                        if dic_mapa[informe_linha][c] == ' ':
                                            qnt_verifica_h += 1 
                                            c += 1
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 2
                                                while c2 <= quantidade+2:
                                                    dic_mapa[informe_linha][c2] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
                                                T += 1 # conta quantas vezes ja pergntou e deu certo
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)
  #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A h 
                                if informe_orientacao == 'v':
                                    c = 0 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade-1:
                                        if dic_mapa[informe_linha+c][2] == ' ':
                                            qnt_verifica_h += 1
                                            c += 1 
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 0
                                                while c2 <= quantidade-1:
                                                    dic_mapa[informe_linha+c2][2] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
   #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A v
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)  







                             # LETRA D
                            if informe_letra == 'D' or informe_letra == 'd':
                                if informe_orientacao == 'h':
                                    #verificar se cabe o navio com a qnt de blocos 
                                    c = 3 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade+3:
                                        if dic_mapa[informe_linha][c] == ' ':
                                            qnt_verifica_h += 1 
                                            c += 1
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 3
                                                while c2 <= quantidade+3:
                                                    dic_mapa[informe_linha][c2] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
                                                T += 1 # conta quantas vezes ja pergntou e deu certo
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)
  #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A h 
                                if informe_orientacao == 'v':
                                    c = 0 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade-1:
                                        if dic_mapa[informe_linha+c][3] == ' ':
                                            qnt_verifica_h += 1
                                            c += 1 
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 0
                                                while c2 <= quantidade-1:
                                                    dic_mapa[informe_linha+c2][3] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
   #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A v
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)  








                             # LETRA E
                            if informe_letra == 'E' or informe_letra == 'e':
                                if informe_orientacao == 'h':
                                    #verificar se cabe o navio com a qnt de blocos 
                                    c = 4 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade+4:
                                        if dic_mapa[informe_linha][c] == ' ':
                                            qnt_verifica_h += 1 
                                            c += 1
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 4
                                                while c2 <= quantidade+4:
                                                    dic_mapa[informe_linha][c2] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
                                                T += 1 # conta quantas vezes ja pergntou e deu certo
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)
  #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A h 
                                if informe_orientacao == 'v':
                                    c = 0 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade-1:
                                        if dic_mapa[informe_linha+c][4] == ' ':
                                            qnt_verifica_h += 1
                                            c += 1 
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 0
                                                while c2 <= quantidade-1:
                                                    dic_mapa[informe_linha+c2][4] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
   #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A v
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)  









                             # LETRA F
                            if informe_letra == 'F' or informe_letra == 'f':
                                if informe_orientacao == 'h':
                                    #verificar se cabe o navio com a qnt de blocos 
                                    c = 5 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade+5:
                                        if dic_mapa[informe_linha][c] == ' ':
                                            qnt_verifica_h += 1 
                                            c += 1
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 5
                                                while c2 <= quantidade+5:
                                                    dic_mapa[informe_linha][c2] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
                                                T += 1 # conta quantas vezes ja pergntou e deu certo
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)
  #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A h 
                                if informe_orientacao == 'v':
                                    c = 0 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade-1:
                                        if dic_mapa[informe_linha+c][5] == ' ':
                                            qnt_verifica_h += 1
                                            c += 1 
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 0
                                                while c2 <= quantidade-1:
                                                    dic_mapa[informe_linha+c2][5] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
   #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A v
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)  









                             # LETRA G
                            if informe_letra == 'G' or informe_letra == 'g':
                                if informe_orientacao == 'h':
                                    #verificar se cabe o navio com a qnt de blocos 
                                    c = 6 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade+6:
                                        if dic_mapa[informe_linha][c] == ' ':
                                            qnt_verifica_h += 1 
                                            c += 1
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 6
                                                while c2 <= quantidade+6:
                                                    dic_mapa[informe_linha][c2] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
                                                T += 1 # conta quantas vezes ja pergntou e deu certo
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)
  #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A h 
                                if informe_orientacao == 'v':
                                    c = 0 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade-1:
                                        if dic_mapa[informe_linha+c][6] == ' ':
                                            qnt_verifica_h += 1
                                            c += 1 
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 0
                                                while c2 <= quantidade-1:
                                                    dic_mapa[informe_linha+c2][6] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
   #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A v
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)  










                             # LETRA H
                            if informe_letra == 'H' or informe_letra == 'h':
                                if informe_orientacao == 'h':
                                    #verificar se cabe o navio com a qnt de blocos 
                                    c = 7 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade+7:
                                        if dic_mapa[informe_linha][c] == ' ':
                                            qnt_verifica_h += 1 
                                            c += 1
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 7
                                                while c2 <= quantidade+7:
                                                    dic_mapa[informe_linha][c2] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
                                                T += 1 # conta quantas vezes ja pergntou e deu certo
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)
  #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A h 
                                if informe_orientacao == 'v':
                                    c = 0 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade-1:
                                        if dic_mapa[informe_linha+c][7] == ' ':
                                            qnt_verifica_h += 1
                                            c += 1 
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 0
                                                while c2 <= quantidade-1:
                                                    dic_mapa[informe_linha+c2][7] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
   #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A v
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)  










                             # LETRA I
                            if informe_letra == 'I' or informe_letra == 'i':
                                if informe_orientacao == 'h':
                                    #verificar se cabe o navio com a qnt de blocos 
                                    c = 8 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade+8:
                                        if dic_mapa[informe_linha][c] == ' ':
                                            qnt_verifica_h += 1 
                                            c += 1
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 8
                                                while c2 <= quantidade+8:
                                                    dic_mapa[informe_linha][c2] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
                                                T += 1 # conta quantas vezes ja pergntou e deu certo
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)
  #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A h 
                                if informe_orientacao == 'v':
                                    c = 0 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade-1:
                                        if dic_mapa[informe_linha+c][8] == ' ':
                                            qnt_verifica_h += 1
                                            c += 1 
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 0
                                                while c2 <= quantidade-1:
                                                    dic_mapa[informe_linha+c2][8] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
   #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A v
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)  












                             # LETRA J
                            if informe_letra == 'J' or informe_letra == 'j':
                                if informe_orientacao == 'h':
                                    #verificar se cabe o navio com a qnt de blocos 
                                    c = 9 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade+9:
                                        if dic_mapa[informe_linha][c] == ' ':
                                            qnt_verifica_h += 1 
                                            c += 1
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 9
                                                while c2 <= quantidade+9:
                                                    dic_mapa[informe_linha][c2] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
                                                T += 1 # conta quantas vezes ja pergntou e deu certo
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)
  #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A h 
                                if informe_orientacao == 'v':
                                    c = 0 
                                    qnt_verifica_h  = 0 
                                    while c <= quantidade-1:
                                        if dic_mapa[informe_linha+c][9] == ' ':
                                            qnt_verifica_h += 1
                                            c += 1 
                                            if qnt_verifica_h  == quantidade:
                                                print ('Navio alocado!')
                                                # pintar todos os blocos do navio 
                                                c2 = 0
                                                while c2 <= quantidade-1:
                                                    dic_mapa[informe_linha+c2][9] = (u"\u001b[42m   \u001b[0m")
                                                    c2 += 1 
   #   #   #     #    #  #   #   #   #    #   #  #print tabuleiro pintado com qnt de blocos de A v
                                        else:
                                            y = 'Não foi possível alocar o navio'
                                            print (y)  


                else: 
                    y = 'Orientação inválida'
                    print (y)
                    chute_jogador (informe_letra, informe_linha, informe_orientacao,quantidade)
            else: 
                y = 'linha invalida'
                print (y)
                chute_jogador (informe_letra, informe_linha, informe_orientacao,quantidade)

        else:
            y = 'coluna invalida'
            print (y)
            chute_jogador (informe_letra, informe_linha, informe_orientacao,quantidade)









# while y == 'coluna invalida':

 #   if y == 'coluna invalida' or y == 'linha invalida':
        


# informe_letra = input('Informe a Letra:')
#informe_linha = input('Informe a Linha:')
# informe_orientacao = input ('Informe a Orientação [v|h]:')




