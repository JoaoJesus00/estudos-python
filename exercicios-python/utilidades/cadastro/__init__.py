from utilidades.dado import leiaint
from utilidades.arquivo import *


def linha():
    print('-' * 40)


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
    tam =  40
    print(c[cor], end='')
    print('-' * tam)
    print(f'{msg.center(tam)}')
    print('-' * tam)
    print(c[0], end='')


def menu(list):
    escreva('MENU PRINCIPAL', )
    c = 1
    for o in list:
        print(f'\033[33m{c}\033[m - \033[34m{o}\033[m')
        c += 1
    linha()
    opc = leiaint('Sua opção: ')
    return opc