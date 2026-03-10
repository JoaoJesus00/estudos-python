with open("algoritmos-estrutura-dados/manipulacao-txt/texto.txt") as text: 
    for linha in text:
        print(linha) #Abre um arquivo txt e nomeia como "text", depois mostra na tela com um loop
        
with open("texto2.txt", "w") as text: #Aqui ele cria um txt, com o mode "w"
    text.write('Hello world!') #.write() para escrever
    
with open("texto2.txt") as text:
    for linha in text:
        print(linha)
        
with open("texto2.txt") as text:
    r = text.readlines()   #Joga o texto do arquivo em uma lista que é a variável "r" 
    
print(r)