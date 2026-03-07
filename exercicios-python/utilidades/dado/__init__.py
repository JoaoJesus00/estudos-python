def leiadinheiro(m):
    v = False
    while not v:
        n = str(input(m)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[0:31mERRO! "{n}" é um preço inválido\033[m')
        else:
            v = True
            return float(n)


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido\033[m')
        if ok:
            break
    return valor

def leiastr(msg):
    while True:
        try:
            s = str(input(msg)).strip()
        except:
            print('\033[0;31mERRO! Digite uma string válida!\033[m')
        else:
            return s