#ENUMERATE - enumera iteráveis(índices)

#[(0, 'William'), (1, 'Ester'), (2, 'Hadassa')]
#É isso que o enumerate faz, cria índices para item da lista
lista = ["William","Ester","Hadassa"]
lista_idade = [['william',34],['ester',26],['hadassa',2]]
lista_enumerada = list(enumerate(lista))
#print(lista_enumerada)

#usando o desempacotamento dentro do for..in
for item in enumerate(lista):
    ind, nome = item
    print(nome)

#Existe outra forma de fazer o desempacotamento direto
for ind, nome in enumerate(lista):
    print(f'Índice: {ind} - Nome: {nome}')