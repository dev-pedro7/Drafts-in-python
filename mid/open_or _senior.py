"""
O Western Suburbs Croquet Club tem duas categorias de membros, Sênior e Aberto. Eles gostariam de sua ajuda com um formulário de inscrição que informará aos possíveis associados em qual categoria eles serão colocados.

Para ser sénior, o sócio deve ter pelo menos 55 anos e ter um handicap superior a 7. Neste clube de croquet os handicaps variam entre -2 e +26; quanto melhor for o jogador, menor será o handicap.

Entrada
A entrada consistirá em uma lista de pares. Cada par contém informações para um único membro potencial. As informações consistem em um número inteiro para a idade da pessoa e um número inteiro para o handicap da pessoa.

Saída
A saída consistirá em uma lista de valores de string (em Haskell e C: Open ou Senior) informando se o respectivo membro será colocado na categoria sênior ou aberta.
"""
def open_or_senior(data):
    categories = []
    for year, cap in data:
        if year >= 55 and cap > 7:
            categories.append("Senior")
        else:
            categories.append("Open")
    return categories
