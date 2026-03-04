num = []
for c in range(0, 5):
    num.append(int(input(f'Digite o {c}º valor: ')))
print(num)
maior = max(num)
menor = min(num)
print(f'Maior valor: {maior} nas posições ', end='')
for c,i in enumerate(num):
    if i == maior:
        print(c, end='...')
print(f'\nMenor valor: {menor} nas posições ', end='')
for c,i in enumerate(num):
    if i == menor:
        print(c, end='...')