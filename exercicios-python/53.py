f = input('Digite uma frase pra saber se é um palíndromo: ').strip().upper()
pal = f.split()
junto = ''.join(pal)
inv = junto[::-1]
print(inv)
if junto == inv:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')