from rich import print
from time import sleep

class Livro:
    def __init__(self, nome, pags):
        self.nome = nome
        self.pags = pags
        self.atual = 1
        print(f':book: [blue]Voce acabou de abrir o livro [green]\'{self.nome}\'[/] que tem [red]{self.pags} páginas[/]. Voce agora está na [yellow]página {self.atual}[/][/]')

    def avançar_pags(self, num=1):
        if (self.atual + num) > self.pags:
            for i in range(self.atual, self.pags + 1):
                print(f'Pág{self.atual}', end=' -> ')
                sleep(0.3)
                self.atual += 1
            print(f'Voce chegou ao final do livro!')
        else:
            for i in range(self.atual, self.atual + num):
                print(f'Pág{self.atual}', end=' -> ')
                sleep(0.3)
                self.atual += 1
            print(f'Voce avançou {num} páginas e agora está na página {self.atual}')

l1 = Livro('10 coisas que eu aprendi', 20)
l1.avançar_pags(5)
l1.avançar_pags(10)
l1.avançar_pags(10)