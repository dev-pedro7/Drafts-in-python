"""
Introdução ao empacotamento e desempacotamento
"""
#_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
#print(nome)

"""
Tipo tupla - Uma lista imutável

nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)
"""
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []

print('Bem vindo a sua lista, oque voce deseja?')

import os

while True:
    opcao = input('inserir, Listar ou apagar:')

    if opcao == 'i' or 'I':
        os.system('cls')
        inserir = input('Digite oque vc quer acrescentar: ')  
        lista.append(inserir)
        
    elif opcao == 'l' or 'L': 
        os.system('cls')
        for num_item, nome_item in enumerate(lista):
            print(num_item, nome_item)

    elif opcao == 'a' or'A':
        os.system('cls')

        try:
            apaga = int(input('digite o numero que você deseja apagar: '))
            del lista[apaga]

        except TypeError:
            print('O valor nao e do tipo esperado.')

        except ValueError:
            print('valor inválido.')    
            
        except IndexError:
            print('índice não está disponível.')
