
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
# print ('5')
# time.sleep(1)
# print ('4')
# time.sleep(1)
# print ('3')
# time.sleep(1)
# print ('2')
# time.sleep(1)
# print ('1')

              
#               PRINT (TABULEIRO) 
