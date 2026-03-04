r1 = float(input('Digite a reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Os segmentos podem formar um: ', end = '')
    if r1 == r2 == r3:
        print('Triângulo Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Não formam um triângulo')