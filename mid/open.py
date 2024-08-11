# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\Users\\Pedro\\Documents\\Python\\mid\\'
caminho_arquivo += 'teste.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()


#ESCREVENDO 'W'
# listar = input('oque voce quer adicionar na anotação?: ')
# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write(listar)
#     # arquivo.write('linha 1\r\n')
#     # arquivo.write('linha 2')

# # LENDO 'R'
# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())
#     print(arquivo.read())

# LENDO E ESCREVENDO 'R+' OU 'W+' 
# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('linha 1\n')
#     arquivo.write('linha 2\n')
#     arquivo.writelines(
#     ('linha 3\n', 'linha 4\n')
#      )  
#    arquivo.seek(0,0)
    #print(arquivo.read())
    # OU o exemplo abaixo para le uma linha de cada
    # print(arquivo.readline(),end='')
    # print(arquivo.readline(),end='')
    # print(arquivo.readline().strip())
    # print(arquivo.readline().strip())

    # readlines
    # for linha in arquivo.readlines():
    #     print(linha.split())        
   
# o 'a' e um .append
# with open(caminho_arquivo, 'a', encoding='utf8') as arquivo:
#      arquivo.write('linhã 5')
#encoding='utf8' serve para conseguirmos colocar caratceres como o ~
     
# import os
# #renomear archive     
# os.rename(caminho_arquivo, 'testenewname.txt')     