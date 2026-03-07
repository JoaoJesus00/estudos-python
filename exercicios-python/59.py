from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
menu = 0
while menu != 5:
    sleep(0.5)
    menu = int(input(f"""--------------------
    {n1} e {n2}
    [1] Somar
    [2] Multiplicar
    [3] maior
    [4] novos números
    [5] sair
---> Digite a operação desejada: """))
    if menu == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif menu == 2:
        print(f'{n1} X {n2} = {n1 * n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print(f'Os números são iguais')
    elif menu == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif menu != 5:
        print('Digite um número válido!')
print('Encerrado!')