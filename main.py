import csv
from datetime import datetime

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
        
        with open('dados.csv', mode='a', newline='') as arquivo_csv:
            
            cabecalhos = ['idade', 'genero', 'pergunta1', 'pergunta2', 'pergunta3', 'pergunta4', 'data_hora']
            escritor_csv = csv.writer(arquivo_csv, delimiter=';')

            if arquivo_csv.tell() == 0:
                escritor_csv.writerow(cabecalhos)

            escritor_csv.writerow([self.idade, self.genero, self.resposta_1, self.resposta_2, self.resposta_3, self.resposta_4, self.data_hora])

def obter_resposta(pergunta):
    
    while True:
        
        resposta = input(f'''
            =============================
                      {pergunta}
            =============================
            1 - Sim
            2 - Não
            3 - Não sei   
            ''')
        
        if resposta in ['1', '2', '3']:
            return resposta
        else:
            print("Por favor, digite uma opção válida (1, 2 ou 3).")

# Abrir o arquivo CSV em modo de escrita, especificando o ponto e vírgula como delimitador
while True:
    
    idade = input('Qual a sua idade? (Digite "00" para encerrar): ')

    if idade != '00':
        
        genero = input('Qual o seu gênero? ')

        print('''
            ======================================
                    PESQUISA DE SEGUROS
            ======================================
            ''')

        resposta_1 = obter_resposta("PERGUNTA 1")
        resposta_2 = obter_resposta("PERGUNTA 2")
        resposta_3 = obter_resposta("PERGUNTA 3")
        resposta_4 = obter_resposta("PERGUNTA 4")

        data_hora = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        
        # Escrever os dados no arquivo CSV
        entrevistado = Pesquisa(idade, genero, resposta_1, resposta_2, resposta_3, resposta_4, data_hora)
        entrevistado.armazenar()

    else:
        print('''
                ===================================
                VOCÊ ENCERROU A COLETA DE DADOS
                ===================================
                ''')
        break
