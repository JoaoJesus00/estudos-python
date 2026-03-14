import numpy as np
# Vetor Ordenado
class VetorOrdenado:
    def __init__(self, capacidade): # A classe é a mesma
        self.capacidade = capacidade
        self.ultima_posiçao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
        
    # O(n)
    def imprime(self):
        if self.ultima_posiçao == -1:
            print('O vetor está vazio!')
        else:
            for i in range(self.ultima_posiçao + 1):
                print(i, ' - ', self.valores[i])
     
    #O(n)           
    def insere(self, valor):
        if self.ultima_posiçao == self.capacidade - 1:  # Verifica se a lista está cheia
            print('Capacidade máxima atingida!')
            return
        posiçao = 0  # Variável pra guardar a posição a ser inserido o valor
        for i in range(self.ultima_posiçao + 1):  # Faz a pesquisa
            posiçao = i  # Vai atualizando a posição
            if self.valores[i] > valor: # Se encontra um elemento maior do que o valor a ser inserido ele faz o break
                break
            if i == self.ultima_posiçao: # Se o valor é maior que todos da lista, para ser inserido no final é preciso atualizar a posição para um índice depois último
                posiçao = i + 1
        x = self.ultima_posiçao # Contador para o while
        while x >= posiçao: # Esse while é para o remanejamento dos elementos
            self.valores[x + 1] = self.valores[x] #Joga os valores pra frente a partir da posição em que o novo elemento será inserido
            x -= 1
        self.valores[posiçao] = valor  # Insere o novo valor
        self.ultima_posiçao += 1  # Atualiza a última posição, que passa para o próximo índice
        

vetor = VetorOrdenado(10)
vetor.insere(6)
vetor.insere(4)
vetor.insere(3)
vetor.insere(5)
vetor.insere(1)
vetor.insere(8)
vetor.imprime()