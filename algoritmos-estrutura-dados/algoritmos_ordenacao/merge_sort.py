# Merge Sort
import numpy as np

def merge_sort(vetor):
    if len(vetor) > 1: # A função só para quando os elementos estão individuais
        divisao = len(vetor) // 2 # Divide o vetor em 2
        esquerda = vetor[:divisao].copy() # Cópia da primeira metade do vetor
        direita = vetor[divisao:].copy() # Cópia da outra metade do vetor
        
        merge_sort(esquerda) # Recursão para ir dividindo o vetor até que os elementos fiquem individuais
        merge_sort(direita)
        # Quando termina a recursão, aqui os elementos estão sozinhos
        
        i = j = k = 0 # Variáveis para controle de indíces
        
        # Ordenação da esquerda e direita:
        while i < len(esquerda) and j < len(direita): # Esse while controla os limites dos subvetores
            # Abaixo ele vai comparando e ordenando no vetor
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1
            
        #  Ordenação final
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1
    
    return vetor
    

print(merge_sort(np.array([15, 34, 8, 3])))
print()
print(merge_sort(np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])))        