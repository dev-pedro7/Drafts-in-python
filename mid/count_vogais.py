def get_count(sentence):
    vogais=("aeiou")
    count = 0
    for i in sentence:
        if i in vogais:
            count += 1
    return count