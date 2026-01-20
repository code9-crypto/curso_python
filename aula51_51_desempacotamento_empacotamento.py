#EMPACOTAMENTO E DESEMPACOTAMENTO
nomes = ['william','ester','hadassa']
print(f"lista de nomes: {nomes}")

#desempacotando toda a lista
nome1, nome2, nome3 = nomes
print(f"desempacotado e atribuido o primeiro nome à variável: {nome1}")

#desempacotando a lista, mas pegando apenas o primeiro nome e empacotando o resto
nome1, *_ = nomes #o * mostra que está pegando o resto da lista e o _ é apenas uma convenção a fim de mostrar que não será usada
print(f"Desempacotado o 1º nome {nome1}\nO resto foi deixado aqui dentro {_}")

#desempacotando apenas um item específico da lista
_, nome2, _, *_ = nomes # aqui está desempacotando apenas o segundo item da lista
print(f"Desempacotado o 2º item da lista: {nome2}")
