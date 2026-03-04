from rich import print

class Funcionario:
    #Atributo de classe
    empresa = 'Curso em Vídeo'
    def __init__(self, nome, setor, cargo):
        #Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return (f':handshake: Olá, meu nome é [blue]{self.nome}[/] e sou '
                f'{self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}!')

c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentacao())

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentacao())