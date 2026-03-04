from rich import print
from rich.panel import Panel

caixa = Panel('[bold yellow]Essa é uma mensagem de exemplo[/] :+1:', title='Mensagem', style='red', width=60)
print(caixa)