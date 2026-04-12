# Shell Sort
import numpy as np

def shell_sort(vetor):
    intervalo = len(vetor) // 2 # Define o gap inicial, quebra o vetor no meio
    
    while intervalo > 0: # Quando o gap chegar a 0, o vetor está ordenado
        for i in range(intervalo, len(vetor)): # Começa do meio para comparar com os elementos de trás
            temp = vetor[i] # Guarda o atual, é o elemento do meio a ser trocado
            j = i # Índice que começa no intervalo e vai andando pra trás, comparando para inserir o temp
            while j >= intervalo and vetor[j - intervalo] > temp: # Acessa o elemento do início para comparar, se ele for maior, entra no while para realizar a troca, quando o j for menor que o intervalo ele sai do while para trocar o elemento da esquerda
                vetor[j] = vetor[j - intervalo] # O elemento da direita recebe o primeiro
                j -= intervalo # O índice passa a ser o da esquerda
            vetor[j] =  temp # O da esquerda recebe o elemento do meio
        intervalo //= 2
    
    print(vetor)
    

shell_sort(np.array([15, 34, 8, 3]))
print()
shell_sort(np.array([9, 8, 7, 6, 5, 4, 3, 2, 1]))