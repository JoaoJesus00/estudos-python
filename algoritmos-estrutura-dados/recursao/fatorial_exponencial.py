# Função para cálculo de fatorial usando Recursividade

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print(fatorial(3))
print(fatorial(4))
print(fatorial(6))
print()

# Função para exponenciação

def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)

print(potencia(2, 2))
print(potencia(2, 3))
print(potencia(2, 4))