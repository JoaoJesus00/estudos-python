print('10 termos de uma PA')
t = int(input('Digite o primeiro termo da PA: '))
r =  int(input('Digite a razão da PA: '))
dec = t + 9 * r
for c in range(t, dec + r, r):
    print(c, end = ' -> ')