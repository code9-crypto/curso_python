# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
# Por padrão o python busca os módulos e pacotes primeiramente no sys.path e depois no próprio pacote

import aula97_m

import sys as s

print(*s.path, sep='\n')
print('Este módulo se chama', __name__)

print(aula97_m.soma(20,50))