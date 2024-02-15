# pessoa = {
#   "nome": "Pedro",
#   "sobrenome": "Miranda",
#   "enderecos": [
#     {
#       "rua": "R1",
#       "numero": 32
#     },
#     {
#       "rua": "R2",
#       "numero": 55
#     }
#   ],
#   "altura": 1.8,
#   "numeros_preferidos": [
#     2,
#     4,
#     6,
#     8,
#     10
#   ],
#   "dev": True,
#   "nada": None
# }
caminho_arquivo = 'C:\\Users\\Pedro\\Documents\\Python\\mid\\'
caminho_arquivo += 'teste.json'
import json
# with open('teste.json', 'w') as archive:
#      json.dump(pessoa, archive)

with open('teste.json', 'r') as archive:
    pessoa = json.load(archive)
    print(pessoa['nome'])