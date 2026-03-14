import numpy as np

# Vetores não ordenados

class VetorNaoOrdenado:  #Classe para criação de um vetor
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posiçao = -1 #Lista começa vazia (índice -1)
        self.valores = np.empty(self.capacidade, dtype=int) #Cria um array vazio do tipo int, e com a capacidade que vai ser definida quando instanciar o objeto.
        
    # O(n)    
    def imprime(self):  #Função para exibir o vetor criado
        if self.ultima_posiçao == -1:
            print('O vetor está vazio!')
        else:
            for i in range(self.ultima_posiçao + 1):
                print(f'{i} - {self.valores[i]}')
           
    # O(1) ou O(2)            
    def insere(self, valor): #Função para inserir valores no vetor
        if self.ultima_posiçao == self.capacidade - 1:
            print('Capacidade máxima atingida!')
        else:
            self.ultima_posiçao += 1 #Esse atributo é para servir de valor do índice
            self.valores[self.ultima_posiçao] = valor
    
    # O(n)   
    def pesquisar(self, valor):
        for i in range(self.ultima_posiçao + 1):
            if valor == self.valores[i]:
                return i
        return -1 # Número inexistente ele retorna -1
    
    # O(n)
    def excluir(self, valor):
        posiçao = self.pesquisar(valor)
        if posiçao == -1:
            return -1  # Se o elemento não existir retorna -1
        for i in range(posiçao, self.ultima_posiçao):
            self.valores[i] = self.valores[i + 1]  # Remanejamento dos elementos
        self.ultima_posiçao -= 1  # Atualiza índice da ultima posição
            
            
vetor = VetorNaoOrdenado(5)
vetor.imprime()
vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)
vetor.insere(7) # Ele não insere pois já atingiu a capacidade máxima
vetor.imprime()
print(vetor.pesquisar(5))
print(vetor.pesquisar(9)) # Pior caso: valor não existente a função percorre a lista inteira
print(vetor.pesquisar(2)) # Melhor caso: valor é o primeiro da lista
vetor.excluir(5)
vetor.imprime()
vetor.excluir(2)
vetor.excluir(1)
vetor.imprime()