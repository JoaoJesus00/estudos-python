from time import sleep
def escreva(msg, cor=0):
    global c
    c = ('\033[m',         # 0: sem cor
         '\033[0:32:40m',  # 1: preto
         '\033[0:30:41m',  # 2: vermelho
         '\033[0:30:42m',  # 3: verde
         '\033[0:30:43m',  # 4: amarelo
         '\033[0:30:44m',  # 5: azul
         '\033[0:30:45m',  # 6: lilás
         '\033[0:30:46m',  # 7: azul
         '\033[0:30:47m')  # 8: cinza
    tam =  len(msg) + 5
    print(c[cor], end='')
    print('-' * tam)
    print(f'{msg.center(tam)}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    escreva(f'Acessando o manual do comando \'{com}\'...', 3)
    print(c[8], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


#Programa principal
while True:
    escreva('SISTEMA DE AJUDA PYHELP', 7)
    com = str(input('Função ou Biblioteca -> '))
    if com.strip().lower() == 'fim':
        break
    else:
        ajuda(com)
escreva('Até logo!', 2)