# Lista Duplamente Encadeada com Extremidades Duplas

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None # Duas referências
        self.anterior = None
        
    def mostra_no(self):
        print(self.valor)
        

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        
    def __lista_vazia(self):
        return self.primeiro == None
    
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo # O nó que estava na lista recebe a referência do novo nó (que será anterior a ele)
        novo.proximo = self.primeiro # O novo nó recebe a referência para apontar para o nó que estava na lista (que será o próximo)
        self.primeiro = novo # Cabeça da lista aponta para o novo nó
        
    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo # Último nó vai apontar para o novo nó inserido no final
            novo.anterior = self.ultimo # Anterior do novo nó vai apontar para o nó que estava por último
        self.ultimo = novo # Referência que aponta para o último nó é atualizada
        
    def excluir_inicio(self):
        temp = self.primeiro
        if self.primeiro.proximo == None: # Se for o único elemento da lista:
            self.ultimo = None # A cabeça da lista vai apontar para None
        else:
            self.primeiro.proximo.anterior = None # O segundo elemento será o primeiro, então a referência para o anterior dele se torna None, pois não terá nada antes dele mais
        self.primeiro = self.primeiro.proximo # Cabeça da lista passa a apontar para o próximo, matando a ligação com o que antes era o primeiro
        return temp
    
    def excluir_final(self):
        temp = self.ultimo
        if self.primeiro.proximo == None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None # O elemento anterior ao último passa a apontar para None, matando a referência do nó a ser excluído, e o anterior ao último passa a ser o último
        self.ultimo = self.ultimo.anterior # Atualiza a referência do último nó
        return temp
    
    def excluir_posicao(self, valor):
        atual = self.primeiro
        while atual.valor != valor: # Percorre até encontrar o valor
            atual = atual.proximo
            if atual == None:
                return None
        if atual == self.primeiro: # Se for o primeiro da lista:
            self.primeiro = atual.proximo # A cabeça da lista passa a apontar para o segundo nó, tornando-o o primeiro
        else: 
            atual.anterior.proximo = atual.proximo # Se está no meio da lista, ele atualiza a referência do nó anterior, apontando para o próximo do nó a ser excluído
        if atual == self.ultimo:
            self.ultimo = atual.anterior # Se for o último, a cabeça da lista passa a apontar para o nó anterior,que se torna o último
        else:
            atual.proximo.anterior = atual.anterior # A referência "anterior" do nó que fica depois do nó excluído passa a apontar para o nó anterior ao excluído
        return atual
        
    def mostrar_frente(self):
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo
            
    def mostrar_tras(self): # Mostra a lista de trás pra frente
        atual = self.ultimo
        while atual != None:
            atual.mostra_no()
            atual = atual.anterior
            


lista = ListaDuplamenteEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.insere_final(9)
lista.insere_final(8)
lista.insere_final(7)
lista.mostrar_frente()
print()
lista.mostrar_tras()
print()
lista.excluir_inicio()
lista.excluir_final()
lista.mostrar_frente()
print()
lista.excluir_posicao(3)
lista.mostrar_frente()