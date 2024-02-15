"""
#elles eliminam valores duplicados ex:
conjuto = {1, 11 ,1 ,1, 2 ,2}


conjuto.add(33)

print(conjuto)

otro = set()
otro.update(('Hello', 1 , 2))
# otro.clear()
#otro.discard('Hello')
print(otro)

"""
#UNIR '|'
# otro = {1, 2, 3, 4,4}
# otra = {3, 4, 5} 
# otre = otro | otra
# print(otre)

# #ITEM PRESENTE EM AMBOS &
# print(otro & otro)

# #ITENS QUE NSO ESTAO EM AMBOS
# print(otra ^ otro)
lista_de_liesta_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],

]
def encontra_primeiro_duplicao(lista_inteiros):
    numeros_checado = set()
    primeir_duplicado = -1

    for numero in lista_inteiros:
        if numero in numeros_checado:
            primeir_duplicado = numero
            break

        numeros_checado.add(numero)
    return primeir_duplicado
for lista in lista_de_liesta_inteiros:
    print(lista, encontra_primeiro_duplicao(lista))