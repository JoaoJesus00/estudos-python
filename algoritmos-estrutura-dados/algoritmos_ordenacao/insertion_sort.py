# Insertion Sort
import numpy as np

def insertion_sort(vetor):
    n = len(vetor)
    for i in range(1, n): # Aqui ele começa no segundo elemento para compará-lo com o primeiro
        marcado = vetor[i] # Elemento marcado começa no segundo do vetor (posição 1)
        j = i - 1 # Variável para percorrer os valores que estão antes do marcado
        while j >= 0 and marcado < vetor[j]: # Esse while vai ser executado até que o elemento marcado seja menor que o elemento do vetor antes dele, ou até que chegue no início do vetor
            vetor[j + 1] = vetor[j] # Remanejamento: os elementos vão sendo jogados pra direita
            j -= 1
        vetor[j + 1] = marcado # Valor inserido no indíce devido
    print(vetor)
    

insertion_sort(np.array([15, 34, 8, 3]))
print()
insertion_sort(np.array([9, 8, 7, 6, 5, 4, 3, 2, 1]))