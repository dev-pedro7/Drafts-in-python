"""
Calculo do primeiro dígito do CPF 24572738033
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 

Multiplicar o resultado anterior por 10

Obter o resto da divisão da conta anterior por 11

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""

#O primeiro dígito do CPF 
import random
#cpf_enviado_usuario = ''\
 #   .replace('-','')\
  #  .replace(' ','')\
   # .replace('.','')
for _ in range(10):
    nine_digit =''
    for i in range(9):
        nine_digit += str(random.randint(0, 9))


    contagem_multiplicacao = 10
    resultado = 0
    for digit in nine_digit:
        resultado += int(digit) * contagem_multiplicacao
        contagem_multiplicacao -= 1
    result_1 = (resultado* 10) %11
    result_1 = result_1 if result_1 <= 9  else 0

    #O segundo dígito do CPF 
    ten_digit = nine_digit + str(result_1)
    contagem_multiplicacao = 11
    resultado = 0
    for digit in ten_digit:
        resultado += int(digit) * contagem_multiplicacao
        contagem_multiplicacao -= 1
    result_2 = (resultado* 10) %11
    result_2 = result_2 if result_2 <= 9  else 0

    cpf_gerado_pelo_calculo = f'{nine_digit}{result_1}{result_2}'
    print(cpf_gerado_pelo_calculo)
    #if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    #   print(f'{cpf_enviado_usuario} é válido')
    #else:
    #    print('CPF inválido')

