#Big-O na criação de listas

# O(1000) --> O(n)
#Aqui ele adiciona os elementos um a um de forma manual
def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

print(lista1())



#Na função abaixo, a função range cria de forma automática a lista com o número de elementos desejados, otimizando o código
#Provavelmente O(1)
def lista2():
    return range(1000)

lista = lista2()
print(lista)