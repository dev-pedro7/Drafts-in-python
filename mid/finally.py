"""
print('vou dividir')
pri_num = int(input())
seg_num = int(input())
try:
    result = pri_num / seg_num
    print(result)
except ZeroDivisionError as error:
    print('obs:', error.__class__.__name__, 'no caso de erro por voce tenta dividi por zero')    
finally:
    print('chegou no final')
"""

def zero(z,y):
    if z or y == 0:
        raise ZeroDivisionError('Voce esta tentando dividir por 0')
    return z / y
v = zero(2,2)
print(v)
