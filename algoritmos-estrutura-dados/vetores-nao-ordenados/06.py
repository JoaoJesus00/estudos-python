import numpy as np

# Vetores não ordenados

class VetorNaoOrdenado:  #Classe para criação de um vetor
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posiçao = -1 #Lista começa vazia (índice -1)
        self.valores = np.empty(self.capacidade, dtype=int) #Cria um array vazio do tipo int, e com a capacidade que vai ser definida quando instanciar o objeto.
        
    def imprime(self):  #Função para exibir o vetor criado
        if self.ultima_posiçao == -1:
            print('O vetor está vazio!')
        else:
            for i in range(self.ultima_posiçao + 1):
                print(f'{i} - {self.valores[i]}')
                
    def insere(self, valor): #Função para inserir valores no vetor
        if self.ultima_posiçao == self.capacidade - 1:
            print('Capacidade máxima atingida!')
        else:
            self.ultima_posiçao += 1 #Esse atributo é para servir de valor do índice
            self.valores[self.ultima_posiçao] = valor
        
                
vetor = VetorNaoOrdenado(5)
vetor.imprime()
vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)
vetor.imprime()
vetor.insere(7)
