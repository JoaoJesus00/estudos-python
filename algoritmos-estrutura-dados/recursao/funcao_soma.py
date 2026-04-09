# Função para soma utilizando Recursão

def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma
    
    
print(soma1(5))
    
    
def soma2(n):
    if n == 0: # Define a condição de parada
        return 0
    
    return n + soma2(n - 1) # Retorna o valor mais a função com o número abaixo
# Aqui ele empilha as chamadas da função, diminuindo o "n" até chegar a 0, depois ele volta somando os retornos das chamadas (n + soma2(n - 1))


print(soma2(5))

# Nesse caso a recursão leva mais tempo