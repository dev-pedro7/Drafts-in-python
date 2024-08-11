# def quicksort(array):
#     if len(array) < 2:
#         return array

#     else:
#         pivo = array[0]
#         menores = [i for i in array[1:] if i <= pivo]    
#         maiores = [i for i in array[1:] if i >= pivo]
#     return quicksort(menores)+ [pivo] +quicksort(maiores)

# print(quicksort([4, 3, 2, 8,1]))

texto = ['ABC123', 'abd012', ' ABS111', 'aBb222 ']

for i, d in enumerate(texto):
    print(i,d)


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

while True:
    resposta = input('Quanto é 2+2?     Opções 1, 3, 4, 5')
    
    def caso(cas):
        match cas:
            case '1':
                return 'Errou'
            case '2':
                return 'Errou'
            case '3':
                return 'Errou'
            case '4':
                return 'acertou'
    resultado = caso(resposta)
    print(resultado)

    o = input('Pergunta : Quanto é 5*5? Opções: [25, 55, 10, 51]') 
    repond = '25'
    status = print('Acertou') if o == repond else print('Errou')