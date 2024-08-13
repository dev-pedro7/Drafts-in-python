def find_average(numbers):
    if len(numbers) == 0:
        return
    new_value = sum(numbers) / len(numbers)
    return new_value
lista = [5,10,5]    
print(find_average(lista))

