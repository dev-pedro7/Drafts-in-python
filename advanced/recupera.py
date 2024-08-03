import json
caminho_arquivo = 'C:\\Users\\Pedro\\Documents\\Python\\mid\\'
caminho_arquivo += 'salvando_class.json'

with open('salvando_class.json', 'r') as arquivo:
    person = json.load(arquivo)
    print(person)