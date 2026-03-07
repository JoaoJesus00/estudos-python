n = total = media = soma = maior = menor = 0
c = 'S'
while c in 'S':
    n = int(input('Digite um valor: '))
    total += 1
    soma += n
    if total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = input('Deseja continuar? [S/N] ').strip().upper()
media = soma / total
print(f'{total} valores digitados, a média entre eles é igual à {media:.1f}, o maior valor foi {maior} e o menor foi {menor}')