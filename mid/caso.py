def verificar_opcao(opcao):
    match opcao:
        case 1:
            return "Você escolheu a opção 1."
        case 2:
            return "Você escolheu a opção 2."
        case 3:
            return "Você escolheu a opção 3."
        case _:
            return "Opção inválida."

# Exemplos de uso
print(verificar_opcao(1))  # Saída: Você escolheu a opção 1.
print(verificar_opcao(2))  # Saída: Você escolheu a opção 2.
print(verificar_opcao(3))  # Saída: Você escolheu a opção 3.
print(verificar_opcao(4))  # Saída: Opção inválida.
def dia(day):
    match day:
        case 1:
            return 'segunda'
        case 2:
            return 'terça'
        case 3:
            return 'quarta'
print(dia(1))
print(dia(2))        
print(dia(3))        
