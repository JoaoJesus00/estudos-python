import math
ang = int(input('Digite o valor de um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f"""Seno = {sen:.2f}
Cosseno = {cos:.2f}
Tangente = {tan:.2f}""")