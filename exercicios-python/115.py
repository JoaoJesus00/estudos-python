from utilidades.cadastro import *
from time import sleep

arq = 'pessoas.txt'

if not arquivoexiste(arq):
    criararquivo(arq)
else:
    print(f'Arquivo {arq} encontrado')

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair'])
    if resp == 1:
        escreva('Pessoas cadastradas')
        lerarquivo(arq)
    elif resp == 2:
        escreva('Cadastro de usuário')
        nome = leiastr('Nome: ')
        idade = leiaint('Idade: ')
        cadastrarpessoa(arq, nome, idade)
    elif resp == 3:
        escreva('FIM')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(1)


