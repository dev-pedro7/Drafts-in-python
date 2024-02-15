"""
bgl = ''
for i in 'dw':
    bgl += (f'!{i}')
    print(i)
print(bgl)
"""

"""
for + range
range -> (start, stop, step)
"""
"""
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
"""
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
""" 
"""
import os
tentativas = 0
secret = 'perfume'
acertadas =''
while True:
    
    letra_digit= input('digitw uma letra e veja se esta na palavra secre')
    tentativas += 1
    if len(letra_digit) >1:
        print('digite so uma letra')
        continue
    if letra_digit in secret:
        acertadas += letra_digit
    palavra_formada = ''
    for letra_secret in secret:
        if letra_secret in acertadas:
            palavra_formada += letra_secret
        else:
            palavra_formada += '*' 
    print(palavra_formada)
    if palavra_formada == secret:
        os.system('cls')
        print('Voce ganhou',tentativas)  
        break      
 """
#Escreva uma função chamada calcular_cubo que recebe 
#um número como argumento e retorna o cubo desse número.

cubo = float(input('vou calcular seu numero ao cubo: '))
def calcular_cubo(cub):
    return cub **3
result = calcular_cubo(cubo)
print(result)