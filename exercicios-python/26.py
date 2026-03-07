frase = input('Digite uma frase: ').strip().lower()
print(f'Essa frase tem {frase.count('a')} A(s)')
print(f'Primeiro A está em {frase.find('a') + 1}')
print(f'Último A está em {frase.rfind('a') + 1}')