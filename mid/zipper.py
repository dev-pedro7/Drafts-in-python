# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:

# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
x = ['Salvador', 'Ubatuba', 'Belo Horizonte']
y = ['BA', 'SP', 'MG', 'RJ']
for i in zip(x,y):print(i)
    
from itertools import zip_longest

for x in zip_longest(x,y, ),:print(x)


# SOMA LISTA
t, g = [1 , 2], [2, 1]
juntas = zip(t,g)
somadas = [t + g for t,g in juntas] 
print(somadas)    
