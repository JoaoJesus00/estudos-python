# Lista encadeada simples com Extremidade Dupla

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
    def mostra_no(self):
        print(self.valor)
        
class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        
    def __lista_vazia(self):
        return self.primeiro == None
    
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo # Aqui a diferença é que quando é o primeiro item a ser inserido na lista, a referência para o último é para ele também, pois é o único nó que existe dentro da lista
        novo.proximo = self.primeiro
        self.primeiro = novo
    
    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia(): # Mesma lógica acima
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo # O que era o último recebe a referência para o novo último
        self.ultimo = novo # Referência do último da lista é atualizada para o novo nó inserido no final
        
    def mostrar(self):
        if self.__lista_vazia():
            print('Lista vazia!')
            return
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print('Lista vazia!')
            return
        temp = self.primeiro
        if self.primeiro.proximo == None: # Se tiver só um elemento na lista
            self.ultimo = None # Não teremos referência para um último
        self.primeiro = self.primeiro.proximo # Atualiza a referência
        return temp


lista = ListaEncadeadaExtremidadeDupla()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_final(9)
lista.insere_final(8)
lista.mostrar()
print()
lista.excluir_inicio()
lista.mostrar()