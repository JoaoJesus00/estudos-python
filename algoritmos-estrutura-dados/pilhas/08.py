import numpy as np
# Exercício: validador de expressões
class Pilha: # Mudanças na classe para esse exercício
    def __init__(self, capacidade, tipo=str):
        self.capacidade = capacidade
        self.topo = -1
        # Mudando para array de caracteres
        self.valores = np.empty(self.capacidade, dtype='U')
        
    def __pilha_cheia(self):
         return True if self.topo == self.capacidade - 1 else False
     
    # Mudamos essa função para pública, pois vamos manipular ela na função do validador de expressões
    def pilha_vazia(self): 
         return True if self.topo == -1 else False
     
    def empilhar(self, valor): 
        if self.__pilha_cheia(): 
            print('A pilha está cheia!')
        else:
            self.topo += 1 
            self.valores[self.topo] = valor 
            
    # Modificação para retornar o elemento desempilhado        
    def desempilhar(self): 
        if self.pilha_vazia():
            print('A pilha está vazia')
            return -1
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor 
            
    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1


expressao = str(input('Digite a expressão a ser validada: '))
pilha = Pilha(len(expressao))

for i in range(len(expressao)):
    ch = expressao[i]  # Armazena o caractere do looping atual
    if ch in '({[': # Se for um caractere de abertura, empilha
        pilha.empilhar(ch)
    elif ch in ')}]': # Se for um caractere de fechamento:
        if not pilha.pilha_vazia(): # Primeiro verifica se a pilha está vazia
            chx = str(pilha.desempilhar()) # Se não, desempilha e verifica se casa com o do topo da pilha: 
            if (ch == '(' and chx != ')') or (ch == '{' and chx != '}') or (ch == '[' and chx != ']'): 
                print(f'Erro: {ch} na posição {i}') # Se não casa, retorna mensagem de erro
        else:
            print(f'Erro: {ch} na posição {i}') # Se a pilha estiver vazia, retorna erro
    if not pilha.pilha_vazia: # Se no final a pilha não estiver vazia, quer dizer que está sobrando caractere de abertura
        print('Erro!') # Então exibe mensagem de erro, expressão incorreta