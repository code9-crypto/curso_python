from sys import path

import aula159_packages
from aula159_packages import modulo #esta importação me parece ser a mais inteligente
# from aula159_packages.modulo import * #isso aqui é uma má prática
    
# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
print(aula159_packages.modulo.soma_do_modulo(1, 2)) #esta escrita fica muito grande
print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)