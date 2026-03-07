# Declaração de classes
class Gafanhoto:
    def __init__(self):  # Método Construtor
        # Atributos de instância
        self.nome = ''
        self.idade = 0

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = 'João'
g1.idade = 23
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Jessica'
g2.idade = 21
print(g2.mensagem())


