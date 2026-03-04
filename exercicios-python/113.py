def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[0;31mERRO!\033[m')
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[0;31mERRO!\033[m')
        else:
            return n


n = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'Inteiro = {n},  Real = {n2}')