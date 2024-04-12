import csv
lista = []
arquivo_csv = open('dados.csv', 'w')
escritor = csv.writer(arquivo_csv)


class Pesquisa:
    def __init__(self, idade, genero, resposta_1, resposta_2, resposta_3, resposta_4, data_hora):
        self.idade = idade
        self.genero = genero
        self.resposta_1 = resposta_1
        self.resposta_2 = resposta_2
        self.resposta_3 = resposta_3
        self.resposta_4 = resposta_4
        self.data_hora = data_hora

    def armazenar(self):
        lista.append([self.data_hora, self.idade, self.genero, self.resposta_1, self.resposta_2,self.resposta_3,self.resposta_4])
       
    


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
            
            while resposta_1 != '1' and resposta_1 != '2' and resposta_1 != '3':
                resposta_1 = input('''
                    =============================
                            PERGUNTA 1
                    =============================
                    1 - Sim
                    2 - Não
                    3 - Não sei          
                    ''')
            
            while resposta_2 != '1' and resposta_2 != '2' and resposta_2 != '3':
                resposta_2 = input('''
                    =============================
                            PERGUNTA 2
                    =============================
                    1 - Sim
                    2 - Não
                    3 - Não sei
                    ''')

            while resposta_3 != '1' and resposta_3 != '2' and resposta_3 != '3':
                resposta_3 = input('''
                    =============================
                            PERGUNTA 3
                    =============================
                    1 - Sim
                    2 - Não
                    3 - Não sei
                    ''')   

            while resposta_4 != '1' and resposta_4 != '2' and resposta_4 != '3':
                resposta_4 = input('''
                    =============================
                            PERGUNTA 4
                    =============================
                    1 - Sim
                    2 - Não
                    3 - Não sei
                    ''')
        
        else:
            print('''
                ===================================
                    VOCÊ ENCERROU A COLETA DE DADOS
                ===================================
                ''')
            break

        entrevistado = Pesquisa(idade, genero, resposta_1, resposta_2, resposta_3, resposta_4, 'código data e hora')
        entrevistado.armazenar()

menu()
print(lista)
for usuario in lista:
        escritor.writerow([usuario])
arquivo_csv.close()