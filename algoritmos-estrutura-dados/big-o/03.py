from math import log
import numpy as np
import matplotlib.pyplot as plt

# Comparação com gráfico de velocidade das funções Big-O conforme entrada aumenta

n = np.linspace(1, 10, 100) #Gera 100 números que vão de 1 até 10
labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential'] #Nomes das funções Big-O
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n] #Cálculos dessas funções para aplicar na lista gerada


for c,i in enumerate(big_o):   #Mostra na tela as tabelas com as funções aplicadas
    print(f'Big-O --> {labels[c]}')
    print(i)
    
plt.figure(figsize=(10,8)) #Criação do gráfico
plt.ylim(0, 100)
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
plt.show()