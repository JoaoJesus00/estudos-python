# Implementação da classe Nó

class No:
    def __init__(self, valor):
        self.valor = valor # Valor do nó
        self.proximo = None # Refêrencia para o próximo da lista
        
    def mostra_no(self):
        print(self.valor)
        

# Classe para armazenar a estrutura desses nós:
class ListaEncadeada:
    def __init__(self):
        self.primeiro = None # Cabeça da lista
        
    def insere_inicio(self, valor): # Sempre adiciona no início da lista (topo)
        novo = No(valor) # Cria o objeto nó
        novo.proximo = self.primeiro # O próximo do novo elemento passa a apontar para o que era o primeiro da lista
        self.primeiro = novo # Cabeça da lista passa a apontar para o novo nó, essa variável sempre aponta para o primeiro da lista
        
    def mostrar(self):
        if self.primeiro == None:
            print('A lista está vazia!')
            return None
        atual = self.primeiro # Recebe a referência apontando para o primeiro
        while atual != None: # None é quando chega no final, em que a refêrencia aponta pra None
            atual.mostra_no() 
            atual = atual.proximo # Atual recebe o proximo do próprio nó, que é a referência do seguinte
            
    def excluir_inicio(self):
        if self.primeiro == None:
            print('A lista está vazia!')
            return None
        temp = self.primeiro # Variável para retornar o elemento excluído
        self.primeiro = self.primeiro.proximo # A referência do primeiro passa a ser a refêrencia que está no primeiro nó, que aponta para o próximo
        # O sistema de exclusão apenas sobrescreve a referência
        return temp # Retorna o item excluído
    
    def pesquisa(self, valor):
        if self.primeiro == None:
            print('A lista está vazia!')
            return None
        atual = self.primeiro # Acessa sempre através do primeiro objeto
        while atual.valor != valor: # Percorre um por um até encontrar o valor pesquisado
            if atual.proximo == None: # Se chega ao fim da lista, o último nó aponta para None
                print('Não encontrado') # Então não foi encontrado
                return None
            else:
                atual = atual.proximo
        print(f'{valor} encontrado no endereço {atual}')
        return
    
    def excluir_posicao(self, valor):
        if self.primeiro == None:
            print('A lista está vazia!')
            return None
        atual = self.primeiro
        anterior = self.primeiro # Precisamos do anterior para sobrescrever a referência dele depois de excluírmos o atual
        while atual.valor != valor:
            if atual.proximo == None:
                print('Não encontrado!')
                return None
            else:
                anterior = atual # Aqui ele atualiza para que o anterior fique um nó atrás do atual
                atual = atual.proximo # Atual passa para o próximo nó
        if atual == self.primeiro: # Se for o primeiro da fila, atualizamos a cabeça da lista para apontar para o próximo
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo # Aqui sobrescrevemos a referência do anterior para o próximo do item excluído
        return atual # Retorna o elemento excluído
        # A variável "anterior" muda o atributo "proximo" do objeto nó, através do "anterior.proximo"
        
    

lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar()
print(lista.excluir_inicio())
lista.mostrar()
lista.pesquisa(3)
lista.pesquisa(7)
lista.excluir_posicao(2)
lista.mostrar()