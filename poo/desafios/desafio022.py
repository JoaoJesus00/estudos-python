# Controle Remoto
from rich import print
from rich.panel import Panel

class Controle:
    canal_min = 1
    canal_max = 6
    volume_min = 1
    volume_max = 5
    def __init__(self, canal=1, volume=2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False
        
    def liga_desliga(self):
        self.ligado = not self.ligado
        
    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == Controle.canal_max:
                self.canal_atual = Controle.canal_min
            else:
                self.canal_atual += 1
        
    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == Controle.canal_min:
                self.canal_atual = Controle.canal_max
            else:
                self.canal_atual -= 1
    
    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != Controle.volume_max:
                self.volume_atual += 1
    
    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != Controle.volume_min:
                self.volume_atual -= 1
    
    def mostrar_tv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = f':prohibited: [red]TV desligada [/red]'
        else:
            conteudo = f'CANAL = '
            for canal in range(Controle.canal_min, Controle.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f'[yellow on yellow] {canal} [/]'
                else:
                    conteudo += f' {canal} '
            conteudo += f'\n'        
            conteudo += f'\nVOLUME = '
            for volume in range(Controle.volume_min, Controle.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f'[black on cyan]   [/]'
                else:
                    conteudo += f'[black on white]   [/]'

            
        tv = Panel(conteudo, title='[ TV ]', width=40)
        print(tv)
        
tv = Controle()

while True:
    tv.mostrar_tv()
    comando = str(input(f'\n < CH{tv.canal_atual} >   - VOL{tv.volume_atual} +  '))
    match comando:
        case '0':
            break
        case '@':
            tv.liga_desliga()
        case '>':
            tv.canal_mais()
        case '<':
            tv.canal_menos()
        case '-':
            tv.volume_menos()
        case '+':
            tv.volume_mais()
    print('\n' * 10)