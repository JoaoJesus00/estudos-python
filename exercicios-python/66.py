s = t = 0
while True:
    n = int(input('Digite um valor [999 para encerrar]: '))
    if n == 999:
        break
    t += 1
    s += n
print(f'{t} números digitados, a soma entre eles é {s}')
