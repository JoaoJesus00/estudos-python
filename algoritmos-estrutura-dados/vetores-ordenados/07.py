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
     
     
    # O(n)           
    def insere(self, valor):
        if self.ultima_posiçao == self.capacidade - 1:  # Verifica se a lista está cheia
            print('Capacidade máxima atingida!')
            return
        # For abaixo é para encontrar a posição
        posiçao = 0  # Variável pra guardar o índice a ser inserido o valor
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
     
    # O(n)   
    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posiçao + 1):
            if self.valores[i] > valor: # Se o primeiro valor já for maior que o da pesquisa, quer dizer que o elemento pesquisado não existe no vetor
                return -1
            if  self.valores[i] == valor:
                return i
            if i == self.ultima_posiçao: # Se percorre a lista toda e não encontra o elemento retorna -1
                return -1
            
    
    # O (log n)
    def pesquisa_binaria(self, valor):
        limite_inferior = 0 # Definimos o ínicio e fim
        limite_superior = self.ultima_posiçao
        
        while True:
            posiçao_atual = int((limite_inferior + limite_superior) / 2) # Divide por 2 pra achar o meio
            if self.valores[posiçao_atual] == valor: # Verifica se esse meio é o valor buscado
                return posiçao_atual
            elif limite_inferior > limite_superior: # Aqui entra se o elemento não está no vetor
                return -1
            else:
                # Limite inferior
                if self.valores[posiçao_atual] < valor: # O valor pequisado é maior que o meio
                    limite_inferior = posiçao_atual + 1
                # Limite superior
                else:
                    limite_superior = posiçao_atual - 1 # O valor pesquisado é menor que o meio
    
    # O(n)
    def excluir(self, valor): # Exatamente igual a função do vetor não ordenado
        posiçao = self.pesquisar(valor) # A única diferença está aqui nessa função pesquisar()
        if posiçao == -1:
            return -1  
        for i in range(posiçao, self.ultima_posiçao):
            self.valores[i] = self.valores[i + 1]  
        self.ultima_posiçao -= 1  
        
"""
vetor = VetorOrdenado(10)
vetor.insere(6)
vetor.insere(4)
vetor.insere(3)
vetor.insere(5)
vetor.insere(1)
vetor.insere(8)
vetor.imprime()
print()
print(vetor.pesquisa_linear(3))
print(vetor.pesquisa_linear(8))
print(vetor.pesquisa_linear(9))
"""

vetor2 = VetorOrdenado(10)
vetor2.insere(8)
vetor2.insere(9)
vetor2.insere(4)
vetor2.insere(1)
vetor2.insere(5)
vetor2.insere(7)
vetor2.insere(11)
vetor2.insere(13)
vetor2.insere(2)
vetor2.imprime()
print()
print(vetor2.pesquisa_binaria(7))
print(vetor2.pesquisa_binaria(5))
print(vetor2.pesquisa_binaria(13))
print(vetor2.pesquisa_binaria(20))