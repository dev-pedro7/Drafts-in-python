# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# def filtrar_preco(produto):
#     return produto['preco'] > 10   


# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# ]
# novos_produtos = filter(
#     lambda produto: produto['preco'] <= 10,
#     produtos
# )


# print_iter(produtos)
# print_iter(novos_produtos)


# reduce
from functools import reduce

# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']


total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print('Total é', total)


# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))




# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
def recursiva(inicio=0, fim=4):

    print(inicio, fim)

    # Caso base
    if inicio >= fim:
         return fim

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())


#                           FATORAÇÃO NO PYTHON:

def factorial(f):
    if f <= 1:
        return 1
    
    return f * factorial(f - 1)

print(factorial(5))