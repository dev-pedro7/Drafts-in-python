def add_binary(a,b):
    c = a + b
    return bin(c).replace("0b", '')
print(add_binary(2,2))