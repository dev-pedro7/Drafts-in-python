
# var = 1, 2
# print(sum(var))

"""
 SHALLOW COPY OR COPIA RASA 
 ------------
d1 = {
    'c1' : 1,
    'c2' : 2,
}
d2 = d1.copy()

d2['c1'] = 11

print(d1)
print(d2)
"""



# DEEP COPY OR COPIA PROFUNDA

import copy
d1 = {
    'c1' : 1,
    'c2' : 2,
}
d2 = copy.deepcopy(d1)

d2['c1'] = 11

# print(d1)
# print(d2)
def f(*kwargs):
    kwargs + kwargs

print(f(1, 2))