import numpy as np

# Pilha

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade           # __ -> Método privado
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)
        
    def __pilha_cheia(self):  # Funções privadas para utilização dentro dos métodos da classe, o usuário não precisa ter acesso
         return True if self.__topo == self.__capacidade - 1 else False
     
    def __pilha_vazia(self): 
         return True if self.__topo == -1 else False
     
    def empilhar(self, valor): 
        if self.__pilha_cheia(): # Verifica se a pilha está cheia
            print('A pilha está cheia!')
        else:
            self.__topo += 1  # Atualiza o topo
            self.__valores[self.__topo] = valor # Adiciona o elemento
            
    def desempilhar(self): 
        if self.__pilha_vazia(): # Verifica se a pilha está vazia
            print('A pilha está vazia')
        else:
            self.__topo -= 1  # Decrementa o topo
            
    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1
        
"""
pilha = Pilha(5)
pilha.empilhar(1)
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
print(pilha.ver_topo())
pilha.empilhar(6)
print(pilha.ver_topo())
pilha.desempilhar()
print(pilha.ver_topo())
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
print(pilha.ver_topo())
pilha.desempilhar()
pilha.desempilhar()
"""