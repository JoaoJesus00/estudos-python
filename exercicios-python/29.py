vel = int(input('Digite a velocidade do carro em km/h: '))
if vel > 80:
    print('Você foi multado por excesso de velocidade!')
    print(f'Valor da multa: R${7 * (vel - 80):.2f}')
else:
    print('Velocidade dentro do limite')