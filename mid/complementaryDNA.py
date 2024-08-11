def DNA_strand(dna):
    complementy = ""
    for i in dna:
        if i == "A":
            complementy += "T"
        elif i == "T":
            complementy += "A"
        if i == "C":
            complementy += "G"
        elif i == "G":
            complementy += "C" 
    return complementy
DNA_strand("AAAA")
    
def no_space(x):
    return x.replace(" ", '')

print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))


def abbrev_name(name):
    first = name[0].upper()
    last = name[-1].upper()
    return f"{first}.{last}"
print(abbrev_name("Pedro Henrique"))

texto = "Pedro Henrique Silva"
partes = texto.split()
print(partes)

def invert(lst):
    return [-i for i in lst]

print(invert([1, -2, 3, -4, 5]))