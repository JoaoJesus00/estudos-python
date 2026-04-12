from rich import print

class Caneta:
    def __init__(self, cor="azul"):
        self.cor = cor
        self.tampa = True

    def destampar(self):
        self.tampa = False

    def tampar(self):
        self.tampa = True

    def escrever(self, msg):
        cores = {'vermelho': 'red', 'amarelo': 'yellow', 'azul': 'blue', 'verde': 'green'}
        cor_traduzida = cores[self.cor]
        if self.tampa:
            print('Caneta tampada!')
        else:
            print(f'[{cor_traduzida}]{msg}')

    def quebrar_linha(self, n=1):
        for i in range(0, n):
            print()

c1 = Caneta('vermelho')
c2 = Caneta('azul')
c3 = Caneta('verde')
c4 = Caneta('amarelo')

c1.destampar()
c2.destampar()
c3.destampar()
c4.destampar()

c1.escrever('Olá')
c1.quebrar_linha(2)
c2.escrever('Oi')
c3.escrever('Tudo bem?')
c3.quebrar_linha()
c4.escrever('Hello')




    