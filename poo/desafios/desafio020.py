from rich import print
from rich.console import Group
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def ficha(self):
        lista = [f':video_game: [red]{jogo}[/]' for jogo in self.favoritos]
        conteudo = Group(
            f'Nome real: [blue on black] {self.nome} [/]',
            f'Jogos Favoritos:',
            *lista
        )
        print(Panel(conteudo, title=f'Jogador <{self.nick}>', width=30,))

    def add_favorito(self, jogo):
        self.favoritos.append(jogo)

g1 = Gamer('Joao Vitor', 'joaodavmh')
g1.add_favorito('Mario')
g1.add_favorito('Batman')
g1.ficha()

g2 = Gamer('Luana', 'luaprincess')
g2.add_favorito('God of War')
g2.add_favorito('Mario')
g2.add_favorito('Fortnite')
g2.ficha()