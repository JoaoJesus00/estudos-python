palavras = 'Aprender', 'Programar', 'Curso', 'Video', 'Computador', 'Gratis', 'Gafanhoto', 'Teclado', 'Mouse'
for c in palavras:
    print(f'\nNa palavra {c} temos as vogais: ', end='')
    for l in c:
        if l.upper() in 'AEIOU':
            print(f'{l.upper()} ', end='')