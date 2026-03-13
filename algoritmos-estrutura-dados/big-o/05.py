#Combinando Big-O
lista = [1, 2, 3, 4, 5]

def combination(n):  # O(1)
    print(n[0])
    
    for i in range(5): #O(5)
        print(i)
    
    for i in n:  #O(n)
        print(i)
        
    for i in n:  #O(n)
        print(i)
        
    print('Python')  #O(3)
    print('Python')
    print('Python')
    
    
combination(lista)

# O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n)  -->  O(n)
# Como o valor de 'n' é linear e aumenta de acordo com a entrada, podemos simplicar direto para O(n)