"""
l1 = [1,3,4]
l2= [5,6,7]
l3 = l1 + l2
print(l3)
print('ou')
l1.extend(l2)
print(l1)

nome = ['Maria, Ana]
for letra in nome
    print(letra)
"""
"""
lista = ['Paulo', 'Mario', 'rosalia']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))  
"""
"""
nomes = ('Maria', 'Helena', 'Luiz')
new = enumerate(nomes, start= 22)
for o in new:
    print(o)  
    """    
"""
for g, h in enumerate(nomes):
    print(g, h)
    """
"""
Lista de listas e seus índices
as = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
"""        
amores_de_mi_life = [
    'ana,','ana julia,',
    'julia ana,', 'my namorada'
                     
                     
                     
                     ]

print(*amores_de_mi_life)        