def menu():
    idade=''
    while True: 
        idade = input('Qual a sua idade?')
        if idade != '00':
            genero = input('Qual o seu gênero?')

            print('''
                ======================================
                        PESQUISA DE SEGUROS
                ======================================
                ''')
            
            resposta_1=''
            resposta_2=''
            resposta_3=''
            resposta_4=''
            
            while resposta_1 != 'sim' and resposta_1 != 'não' and resposta_1 != 'não sei':
                resposta_1 = input('''
                    =============================
                            PERGUNTA 1
                    =============================
                    Deve ser respondido com sim/não/não sei
                    ''')
            
            while resposta_2 != 'sim' and resposta_2 != 'não' and resposta_2 != 'não sei':
                resposta_2 = input('''
                    =============================
                            PERGUNTA 2
                    =============================
                    Deve ser respondido com sim/não/não sei
                    ''')

            while resposta_3 != 'sim' and resposta_3 != 'não' and resposta_3 != 'não sei':
                resposta_3 = input('''
                    =============================
                            PERGUNTA 3
                    =============================
                    Deve ser respondido com sim/não/não sei
                    ''')   

            while resposta_4 != 'sim' and resposta_4 != 'não' and resposta_4 != 'não sei':
                resposta_4 = input('''
                    =============================
                            PERGUNTA 4
                    =============================
                    Deve ser respondido com sim/não/não sei
                    ''')
        else:
            print('''
                  ===================================
                    VOCÊ ENCERROU A COLETA DE DADOS
                  ===================================
                  ''')
            break  

menu()