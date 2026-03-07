peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print(f'IMC = {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')