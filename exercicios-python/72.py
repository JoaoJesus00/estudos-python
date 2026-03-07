num = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    pergunta = int(input('Digite um número de 0 até 20: '))
    if 0 <= pergunta <= 20:
        break
    print('Valor inválido! ', end='')
print(f'Você digitou o número {num[pergunta]}')
