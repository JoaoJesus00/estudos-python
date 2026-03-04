from time import sleep
def maior(* num):
    print('-=' * 20)
    print('Analisando valores...')
    maior = num[0]
    for v in num:
        sleep(0.3)
        print(v, end=' ')
        if v > maior:
            maior = v
    print(f'\nForam informados {len(num)} valores')
    print(f'O maior valor informado foi {maior}.')

maior(3, 7, 9, 4, 2, 0)