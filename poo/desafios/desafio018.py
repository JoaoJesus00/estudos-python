from rich import print
from rich.panel import Panel

class Churrasco:
    consumo:float = 0.4
    preço_kg:float = 82.40
    def __init__(self, nome, pessoas):
        self.nome = nome
        self.pessoas = pessoas

    def kilototal(self) -> float:
        return Churrasco.consumo * self.pessoas

    def custototal(self) -> float:
        return self.kilototal() * Churrasco.preço_kg

    def custopessoa(self) -> float:
        return self.custototal() / self.pessoas

    def analisar(self):
        conteudo = (f'Analisando [green]{self.nome}[/] com [blue]{self.pessoas} convidados[/]'
         f'\nCada participante comerá {Churrasco.consumo}Kg e cada Kg custa R${Churrasco.preço_kg:.2f}'
         f'\nRecomendo comprar [blue]{self.kilototal()}Kg[/] de carne'
         f'\nO custo total será de [green]R${self.custototal():.2f}[/]'
         f'\nCada pessoa pagará [yellow]R${self.custopessoa():.2f}[/]')
        print(Panel(conteudo,title=self.nome, width=70))

c1 = Churrasco('Churras dos amigos', 15)
c1.analisar()

c2 = Churrasco('Festa de fim de ano', 80)
c2.analisar()