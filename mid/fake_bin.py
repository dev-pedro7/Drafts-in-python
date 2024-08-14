def fake_bin(x):
    resultado = ''
    for i in x:
        if int(i) < 5:
            resultado += '0'
        else:
            resultado += '1'
    return resultado        