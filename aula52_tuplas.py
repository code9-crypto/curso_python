#TUPLAS - lista imutável
#OBS.: tupla é uma lista que não aceita mudança e nem modificação
nomes = ('william', 'ester', 'hadassa') #aqui mostra que é uma tupla
print(f"Aqui é uma tupla: {nomes} -> {type(nomes)}")

#transformando de tupla para lista
nomesList = list(nomes)
print(f"Aqui a tupla foi convertida em lista: {nomesList} -> {type(nomesList)}")

#transformando de lista para tupla
nomeTuple = tuple(nomesList)
print(f"Aqui peguei a lista criado acima e transformei para tupla de novo: {nomeTuple} {type(nomeTuple)}")
