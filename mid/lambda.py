"""
listona = [1 ,2, 3, 677, 8, 1, 5, 76, 7,]
#crescente
listona.sort(reverse=True)
print(listona)
#decrescente
listona.sort(reverse=False)

print(listona)
"""
"""
#Ordena pwlo nome
lista = [
            {'nome': 'Daniel', 'Sobrenome':'Elisberto'},
            {'nome': 'ALINE','Sobrenome':'henrick' },
        ]
def ordena(item):
        return item['nome']

lista.sort(key=ordena)

for item in lista:
    print(item)
#Com Lambda o codigo de cima ira ficar assim
print()   

lista.sort(key=lambda item: item['nome'])
print()
lista.sort(key=lambda item: item['Sobrenome'])

for item in lista:
    print(item)
"""

def executa(funcao, *args):
    return funcao(*args)




def soma(x,y):
    return x+ y
print(soma(2,3))
#  É igual a
print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)





def cra_multiplicador(multiplicador):
    def multiplica(numero):
        return numero* multiplicador
    return multiplica

#  É igual a

duplica = executa(
    lambda m: lambda n: n*m,
    2
)
print(duplica(10))


lista_1 = {
    'nome': 'Claudio',
    'sobrename': 'Claudia'
}

lista_2 = {
    'lati': 'Adailto',
    'cao': 'Adailta'
}
pessoas = {**lista_1}
print(pessoas)