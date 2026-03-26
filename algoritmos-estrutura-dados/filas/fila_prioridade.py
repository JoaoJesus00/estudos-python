import numpy as np

# Fila de Prioridade

class FilaPrioradade: # Esta não é uma fila circular
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)
        # O ínicio da fila fica nos índices mais altos, e o final no índice 0.
        
    def __fila_vazia(self):
        return self.numero_elementos == 0
    
    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    # A prioridade será para números menores:
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Filha cheia')
            return
        if self.numero_elementos == 0: # Se ainda não tem elemento na fila, só insere o valor sem necessidade de remanejamento
            self.valores[self.numero_elementos] =  valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos - 1 # Contador pro while
            while x >= 0: 
                if valor > self.valores[x]: # Se o valor for maior que o elemento atual do laço:
                    self.valores[x + 1] = self.valores[x] # Realiza remanejamento (vai jogando o número maior pra tras da fila e os menores pra frente)
                else: # Se não for maior, quer dizer que encontrou a posição
                    break
                x -= 1
            self.valores[x + 1] = valor # Insere o valor
            self.numero_elementos += 1
            
    def desinfileirar(self):
        if self.__fila_vazia():
            print('Fila vazia!')
            return
        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1 # Somente decrementa o último elemento (primeiro da fila)
        return valor
            
            
    def primeiro(self):
        if self.__fila_vazia():
            print('Fila vazia!')
        else:
            print(self.valores[self.numero_elementos - 1])
            
            
            
fila = FilaPrioradade(5)
# 30
fila.enfileirar(30)
fila.primeiro()
# 50 30
fila.enfileirar(50)
fila.primeiro()
# 50 30 10
fila.enfileirar(10) # Tradicional: 10 50 30
fila.primeiro()     # Prioridade:  50 30 10  < Menor elemento no início
# 50 40 30 10
fila.enfileirar(40)
fila.primeiro()
# 50 40 30 20 10
fila.enfileirar(20)
fila.primeiro()
# 50 40 30 20
fila.desinfileirar()
fila.primeiro()
# 50 40 30
fila.desinfileirar()
fila.primeiro()
# 50 40
fila.desinfileirar()
fila.primeiro()