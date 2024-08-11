def high_and_low(numbers):
    numbers = list(map(int, numbers.split()))
    maxi = max(numbers)
    mini =  min(numbers)  
    return f"{maxi} {mini}"
def make_negative( number ):
    if number > 0:
        -number
    return number    

print(make_negative(42))  
def make_negative(number):
    if number > 0:
        return -number
    return number

# Teste
print(make_negative(42))  # Saída esperada: -42

def century(year):
   if 000 in year:
    return True
print(century(1700))
