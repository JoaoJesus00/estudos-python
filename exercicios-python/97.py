def escreva(msg):
    tam =  len(msg) + 5
    print('-' * tam)
    print(f'{msg.center(tam)}')
    print('-' * tam)

escreva('Joao')
escreva('Curso em Video')