iterable = ['EU', 'adoro', 'iterar']
iterador = iter(iterable)
print(next(iterador))
print(next(iterador))
print(next(iterador))

# generator pegar um valor por vez
"""
gen = ( n for n in 5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""
def generacão(n=0):
    yield 1
    print('continua')
    yield 2
    print('continua dnv')
    yield 3

gene = generacão()
for i in gene:
    print (i)

def generacão(n=0, max=10):
    while True:
        yield n
        n += 1
        if n >= max:
            return

gene = generacão(max=6)
for i in gene:
    print (i)

def gen1():
    yield 1
    yield 2
    
def gen2():
    yield from gen1()
    yield 4
    yield 5

g = gen2()
print(next(g))
print(next(g))    
print(next(g))    
print(next(g))    


    
