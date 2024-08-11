# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# platform = 'A MINHA'
# print(sys.platform)
# print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform

# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as s

# sys = 'alguma coisa'
# print(s.platform)
# print(sys)


# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import exit, platform

# print(platform)
# exit()
"""
import platform

sistema_operacional = platform.system()
print(f"Sistema Operacional: {sistema_operacional}")

versao_sistema = platform.version()
print(f"Versão do Sistema: {versao_sistema}")

arquitetura = platform.architecture()
print(f"Arquitetura: {arquitetura}")
"""
"""
import importlib

import exe

from exe import criar_multiplicador

mult = criar_multiplicador(10)
print(mult(10))

for i in range(10):
    importlib.reload(exe)
    print(i)
"""
from basic.fore import i
print(i)