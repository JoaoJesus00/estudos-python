from utilidades.dado import *

def arquivoexiste(nome):
    try:
        with open(nome, 'rt'):
            pass
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        with open(nome, 'w+'):
            pass
    except:
        print('Erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}\t{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrarpessoa(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'a')
    except:
        print('Erro ao abrir arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao adicionar pessoa')
        else:
            print('Cadastro realizado com sucesso!')


