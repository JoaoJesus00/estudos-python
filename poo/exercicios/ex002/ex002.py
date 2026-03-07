# Declaração de classes
class Gafanhoto:
    #Docstring
    """
    Essa classe cria um Gafanhoto, que é uma pessoa com nome e idade.
    Para criar uma nova pessoa, use:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome='Desconhecido', idade=0):  # Método Construtor
        # Atributos de instância
        self.nome = nome
        self.idade = idade

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): #Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f'{self.nome} = {self.idade} anos'

# Declaração de Objetos
g1 = Gafanhoto('João', 23)
print(g1)
print(g1.__dict__)  #Attribute
print(g1.__getstate__())  #Method
print(g1.__class__)
print(g1.__doc__) #Dunder Attribute

# DUNDER = Double Underline __


