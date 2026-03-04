cid = input('Digite o nome da cidade: ').lower().strip().split()
if 'santo' in cid[:5]:
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')