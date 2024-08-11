def count_sheep(n):
    count = []
    for i in range(1,n + 1):
        count +=  f"{i} sheep..."
    return "".join(count)
    
print(count_sheep(5))