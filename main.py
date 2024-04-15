#importações para facilitar o processo
import csv
from datetime import datetime
import matplotlib.pyplot as plt

#classe para escrever/armazenar no arquivo csv
class Pesquisa:

    #Estrutura para POO
    def __init__(self, idade, genero, resposta_1, resposta_2, resposta_3, resposta_4, data_hora):
        
        self.idade = idade
        self.genero = genero
        self.resposta_1 = resposta_1
        self.resposta_2 = resposta_2
        self.resposta_3 = resposta_3
        self.resposta_4 = resposta_4
        self.data_hora = data_hora

    def armazenar(self):

        #Abre o arquivo CSV em modo de append, especificando o ponto e vírgula como delimitador
        with open('dados.csv', mode='a', newline='') as arquivo_csv:
            
            cabecalhos = ['idade', 'genero', 'pergunta1', 'pergunta2', 'pergunta3', 'pergunta4', 'data_hora']
            escritor_csv = csv.writer(arquivo_csv, delimiter=';')

            if arquivo_csv.tell() == 0:
                escritor_csv.writerow(cabecalhos)

            #escreve na linha
            escritor_csv.writerow([self.idade, self.genero, self.resposta_1, self.resposta_2, self.resposta_3, self.resposta_4, self.data_hora])

def exibir_grafico():

    with open('dados.csv', mode='r', newline='') as arquivo_csv:

        leitor_csv = csv.reader(arquivo_csv, delimiter=';')
        
        # Pular o cabeçalho
        next(leitor_csv)

        qtd_sim, qtd_nao, qtd_nao_sei = 0, 0, 0

        # Passa por cada linha do arquivo
        for linha in leitor_csv:
            
            # Pega as respostas especificas
            r1, r2, r3, r4 = linha[2:6]

            # Atualiza os contadores
            qtd_sim += r1.count('1') + r2.count('1') + r3.count('1') + r4.count('1')
            qtd_nao += r1.count('2') + r2.count('2') + r3.count('2') + r4.count('2')
            qtd_nao_sei += r1.count('3') + r2.count('3') + r3.count('3') + r4.count('3')

        # Dados para o gráfico de pizza
        labels = 'Sim', 'Não', 'Não sei'
        sizes = [qtd_sim, qtd_nao, qtd_nao_sei]
        colors = ['lightcoral', 'lightskyblue', 'yellowgreen']
        explode = (0.1, 0, 0)


#função para validação das perguntas
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

#Menu do usuário
while True:
    
    idade = input('Qual a sua idade? (Digite "00" para encerrar): ')

    if idade != '00':
        
        genero = input('Qual o seu gênero? ')

        print('''
            ======================================
                    PESQUISA DE SEGUROS
            ======================================
            ''')

        #respostas e perguntas
        resposta_1 = obter_resposta("PERGUNTA 1")
        resposta_2 = obter_resposta("PERGUNTA 2")
        resposta_3 = obter_resposta("PERGUNTA 3")
        resposta_4 = obter_resposta("PERGUNTA 4")

        #data e hora da resposta
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
