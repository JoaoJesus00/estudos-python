n = q = s = 0
n = int(input('Digite um valor (999 para encerrar): '))
while n != 999:
    q += 1
    s += n
    n = int(input('Digite um valor (999 para encerrar): '))
print(f'{q} números digitados, a soma entre eles é igual à {s}')