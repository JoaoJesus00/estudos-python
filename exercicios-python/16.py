from math import hypot
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print(f'O valor da hipotenusa é {hipotenusa:.2f}')