# Bubble Sort
import numpy as np

def bubble_sort(vetor):
    n = len(vetor) # Variável armazena o número de elementos do vetor
    for i in range(n): # Esse for é para cada rodada de comparações, ele vai comparar todos os elementos e ordenando no fim da lista os maiores a cada rodada
        # O for debaixo compara cada elemento da rodada com o próximo, indo até o que ja foi ordenado no fim
        for j in range(0, n - i - 1): # Ele só vai até o elemento que não está ordenado, ele não precisa comparar os maiores que já estão no fim do vetor, conforme ele vai definindo os últimos, ele vai desconsiderando eles na comparação
            if vetor[j] > vetor[j + 1]: # Se o vetor da esquerda for maior que o da direito, será feito a troca
                temp = vetor[j] # Faz a cópia do elemento
                vetor[j] = vetor[j + 1] # O da esquerda se torna o da direita
                vetor[j + 1] = temp # O da direita recebe o da esquerda (a cópia "temp")
    print(vetor)
    

bubble_sort(np.array([15, 34, 8, 3]))
print()
bubble_sort(np.array([9, 8, 7, 6, 5, 4, 3, 2, 1]))
