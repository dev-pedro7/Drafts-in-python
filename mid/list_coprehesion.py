# isinstace - para saber se objetp é de determinado tipo ex:
lista = [
    'a', 1, 1.1, True, [0, 1, 2],
    (1, 2), {0, 1}, {'nome':'Luiz'},
    ]
for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item,set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item, type(item))    

"""
lista = []
for numero in range(11):
    lista.append(numero)
print(lista)
#E igual a
lista  = [numero for numero in range(10)]
print(lista)
print()
"""

"""
lista  = [
    numero * 2
    for numero in range(10)
    
]
print(lista)

#FILTROS
produto = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 5,},
    {'nome': 'p3', 'preco': 40,},


]
import pprint
def p(w):
    pprint.pprint(novos_prdoutos, sort_dicts=False, width=40)

novos_prdoutos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produto
    if produto['preco'] >= 20  and produto['preco'] * 1.05 > 10
                ]
p(novos_prdoutos)
"""
"""
produto = {
    'nome': 'Caneta Azul',
    'preco':2.5,
    'categoria': 'escritorio',
}
# Dictionary Comprehension

dc = {
    chave: valor.lower()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}
print(dc)

# Set Comprehension

s1 = {i ** 2 for i in range(10)}
print(s1)
"""