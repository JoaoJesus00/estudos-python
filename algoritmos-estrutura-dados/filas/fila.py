# Implementando a classe de fila
import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0 # Váriavel para o cursor do início
        self.final = -1 # Váriavel para o cursos do final
        self.numero_elementos = 0 # Guarda o número de elementos que estão na fila
        self.valores = np.empty(self.capacidade, dtype=int)
        
    def __fila_vazia(self):
        return self.numero_elementos == 0
    
    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila já está cheia!')
            return
        
        if self.final == self.capacidade - 1: # Se o cursor já está no final:
            self.final = -1 # Atualiza e joga para o outro lado (fila circular);
        self.final += 1 # Atualiza a posição do final:
        self.valores[self.final] = valor # Incrementa o valor nessa posição;
        self.numero_elementos += 1 # Atualiza o número de elementos
        
    def desenfileirar(self):
        if self.__fila_vazia():
            print("Fila já está vazia!")
            return
        
        temp = self.valores[self.inicio] # Joga nessa variável o elemento que vai ser desinfileirado
        self.inicio += 1 # O índice do primeiro da fila passa a ser o próximo
        if self.inicio == self.capacidade - 1: # Mesmo princípio de cima:
            self.inicio = 0        # Se o cursor estiver no limite, ele atualiza para o começo novamente
        self.numero_elementos -= 1 # Atualiza a quantidade de elementos na fila
        return temp # Retorna o elemento desenfileirado para vizualização
    
    def primeiro(self):
        if self.__fila_vazia():
            return -1
        print(self.valores[self.inicio])
    
    
fila = FilaCircular(5)

# 1
fila.enfileirar(1)
fila.primeiro()

# 2 1
fila.enfileirar(2)
fila.primeiro()

# 5 4 3 2 1
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)

# 5 4 3 2
fila.desenfileirar()
# 5 4 3
fila.desenfileirar()

fila.primeiro()

# 6 5 4 3
fila.enfileirar(6)
# 7 6 5 4 3
fila.enfileirar(7)

fila.primeiro()

print(fila.valores) # Aqui podemos ver a fila circular, cursor início está no índice 2, e o cursor final está no indíce 1