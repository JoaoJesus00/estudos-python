n = int(input('Digite um número inteiro: '))
c = int(input("""Escolha a base de conversão:
1. Binário
2. Octal
3. Hexadecimal
Digite o número da operação desejada: """))
if c == 1:
    print(f'{c} em binário é igual a: {bin(n)[2:]}')
elif c == 2:
    print(f'{c} em Octal é igual a: {oct(n)[2:]}')
elif c == 3:
    print(f'{c} em Hexadecimal é igual a: {hex(n)[2:]}')
else:
    print('Digite um número válido!')