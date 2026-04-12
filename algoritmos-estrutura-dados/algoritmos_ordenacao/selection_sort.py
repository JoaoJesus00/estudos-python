# Selection Sort
import numpy as np

def selection_sort(vetor):
    n = len(vetor)
    for i in range(n): # Esse for é pra cada rodada de comparação, a cada rodada ele irá procurar o mínimo para jogar pro início do vetor
        id_minimo = i # Variável pra guardar o indíce do menor valor encontrado, recebe i para começar do primeiro elemento
        for j in range(i + 1, n): # Aqui definimos o range assim para não percorrermos os elementos que já estão ordenados no início do vetor, a cada rodada o for começa um indíce à frente (i + 1), esse for compara os elementos e guarda o indíce do menor
            if vetor[id_minimo] > vetor[j]:
                id_minimo = j
        temp = vetor[i] # Cópia do elemento inicial de cada rodada
        vetor[i] = vetor[id_minimo] # Elemento inicial de cada rodada se torna o menor valor encontrado
        vetor[id_minimo] = temp # Onde estava o valor mínimo se torna o elemento que estava no ínicio, ou seja, é realizado uma troca
    print(vetor)
    

selection_sort(np.array([15, 34, 8, 3]))
print()
selection_sort(np.array([9, 8, 7, 6, 5, 4, 3, 2, 1]))        