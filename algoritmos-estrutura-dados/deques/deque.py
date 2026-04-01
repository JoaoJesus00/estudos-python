# Implementação da classe Deque
import numpy as np

class Deque: # Construtor igual ao da fila
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1 # Deque é circular dentro do vetor
        self.final = 0
        self.numero_elementos = 0
        self.valores = np.empty(capacidade, dtype=int)
        
    def __deque_cheio(self):
        return self.numero_elementos == self.capacidade
    
    def __deque_vazio(self):
        return self.numero_elementos == 0
    
    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print('Deque já está cheio!')
            return
        # Se o deque estiver vazio:
        if self.__deque_vazio():
            self.inicio = 0
            self.final = 0 # O valor será o primeiro e o último
        # Se o ínicio estiver na primeira posição:
        elif self.inicio == 0:
            self.inicio = self.capacidade - 1 # Início passa pro outro lado do vetor (circular)
        else:
            self.inicio -= 1 # Senão só atualiza o índice

        self.valores[self.inicio] = valor
        self.numero_elementos += 1
        
    def insere_final(self, valor):
        if self.__deque_cheio():
            print('Deque já está cheio!')
            return
        if self.__deque_vazio():
            self.inicio = 0
            self.final = 0
        # Se o final estiver na última posição (limite do vetor):
        elif self.final == self.capacidade - 1:
            self.final = 0 # Final passa pro lado esquerdo do vetor
        else:
            self.final += 1
            
        self.valores[self.final] = valor
        self.numero_elementos += 1
        
    def excluir_inicio(self):
        if self.__deque_vazio():
            print('Deque já está vazio!')
            return
        # Se possui apenas um elemento:
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1  # Reseta o deque
        elif self.inicio == self.capacidade -1: # Se estiver no limite do vetor:
            self.inicio = 0 # Volta pro lado esquerdo
        else:
            self.inicio += 1
        self.numero_elementos -= 1
                
    def excluir_final(self):
        if self.__deque_vazio():
            print('Deque já está vazio!')
            return
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        elif self.final == 0:
            self.final = self.capacidade - 1
        else:
            self.final -= 1
        self.numero_elementos -= 1
            
    def get_inicio(self):
        if self.__deque_vazio():
            print('Deque está vazio!')
            return       
        print(self.valores[self.inicio])
        
    def get_final(self):
        if self.__deque_vazio():
            print('Deque está vazio!')
            return       
        print(self.valores[self.final])
        

deque = Deque(5)
# 5
deque.insere_final(5)

# 5 10
deque.insere_final(10)

# 3 5 10
deque.insere_inicio(3)

# 2 3 5 10 11
deque.insere_inicio(2)
deque.insere_final(11)
deque.get_inicio(), deque.get_final()
print()

# 3 5 10
deque.excluir_inicio()
deque.excluir_final()
deque.get_inicio(), deque.get_final()