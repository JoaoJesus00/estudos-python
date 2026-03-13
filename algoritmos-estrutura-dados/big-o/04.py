#Exemplos de funções Big-O

lista = [1, 2, 3, 4, 5]

# O(1) --> Constant
def constant(n):
    print(n[0])
    
constant(lista)
# Veja que independente do número de 'n', a função sempre vai executar apenas um número fixo de passos, que nesse caso é apenas um passo, que é mostrar o primeiro elemento da lista.


# O(n) --> Linear
def linear(n):
    for i in n:
        print(i)

linear(lista)
# Aqui o número de passos aumenta conforme a entrada ('n'), nesse caso 5 passos, se a lista tivesse 50 elementos, seriam 50 passos.


# O(n^2) --> Quadratic

def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
        print('---')

quadratic(lista)
# Na função quadrática o tempo de execução cresce proporcionalmente ao quadrado da entrada (n). Nesse caso, a cada looping a lista é percorrida, executando 5 passos, no fim de 5 loopings, o total é de 25 passos, que é o quadrado da entrada 5.