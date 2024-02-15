

# def multiplicar(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total


# a = multiplicar(10,10)
# print(a)

# def par_impar(z):
#     par = z % 2 
#     if par is 0:
#         return 'Par'
#     else:
#         return 'Impar'

# print(par_impar(6))    

# def duplica(z):
#     return z * 2

# print(duplica(2))    

# def triplica(y):
#     return y * 3

# print(triplica(2))    

# def quadriplica(x):
#     return x * 4

# print(triplica(4))    

#or
"""
print(123)
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
"""
"""
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))    
"""

prod = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

import copy

# Aumente os preços dos produtos a seguir em 10%
dez = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(prod)
]
print(*dez, sep='\n')

print()

# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = copy.deepcopy(prod)
novos_produtos.append({'nome': 'Produto 4', 'preco': 80.00})
print(*novos_produtos, sep='\n')

print()

# Ordene os produtos por nome decrescente (do maior para menor)
sorted_list = sorted(novos_produtos, key=lambda x: x['nome'], reverse=True)
print(*sorted_list, sep='\n')

print()

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda) and
# Ordene os produtos por preco crescente (do menor para maior)

new = sorted(novos_produtos, key=lambda x: x['nome'], reverse=False)
produtos_ordenados_por_nome = copy.deepcopy(new)
print(*produtos_ordenados_por_nome, sep='\n')

print()

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
new_of_preco = sorted(novos_produtos, key=lambda x: x['preco'], reverse=True)
produtos_ordenados_por_preco = copy.deepcopy(new_of_preco)
print(*produtos_ordenados_por_preco, sep='\n')
