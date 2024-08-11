# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
"""
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
"""
# print(pessoa['nome'])
# print(pessoa['sobrenome'])

# for chave in pessoa:
#     print(chave, pessoa[chave])
# for pessoas, valor in pessoa.items():
#     print(pessoas, valor)
# pessoa.setdefault('idade', 16)
# print(pessoa['idade'])



acertos = 0
pergunta =[
            {
    'nome': 'Quantos é 10 + 10',
    'opcao' : ['20', '10', '100'],
    'resposta': '20'
},
            {
    'nome': 'Quantos é 5 * 5',
    'opcao' : ['25', '50', '30'],
    'resposta': '25'

}
]
for chave in pergunta:
    print(chave['nome'])
    
    
    for i, alternativas in enumerate(chave['opcao']):
        print(f'{i})', alternativas)

    print()

    escolha = input('Escolha uma opcao: ')
    if escolha == pergunta('resposta'):
        print( 'Acerto')
        acertos   += 1
    else:
        print( 'erro') 


print(f'Voce acertou {acertos} '\
      'de', len(pergunta))