#Comparando algoritmos através de Big-O

#Função 1 - O(n)

def soma(n):  #11 passos
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

print(soma(10))
time = timeit.timeit(soma(10), number=10000)
print(time)
#Aqui a complexidade aumenta de acordo com a entrada, nesse caso O(11)



#Função 2

# O(3)
def soma(n): #3 passos: (multiplicação, soma e divisão)
    return n * (n + 1) / 2

print(soma(10))
#Aqui a função executará sempre 3 passos, independente da entrada



#Listas O(n) X Dicionários O(1)

usuarios_lista = ['joao', 'pedro', 'gustavo', 'maria']
for i in usuarios_lista:
    if i == 'maria':
        print('Achei')
    else:
        print('Não achei')
     
     
        
usuarios_dict = {'joao': 'Perfil A', 'pedro': 'Perfil B', 'gustavo': 'Perfil C', 'maria': 'Perfil D'}
perfil = usuario_dict['joao']
print(perfil)