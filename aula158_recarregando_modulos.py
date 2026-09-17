import importlib

import aula97_m

print(aula97_m.variavel)

for i in range(10):
    importlib.reload(aula97_m)
    print(i)

print('Fim')