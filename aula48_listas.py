'''
Tipo list - Mútavel
Métodos úteis: append, insert, pop, del, clear, extend, +
append - adiciona item no final da lista
insert - adiciona item no índice escolhido
pop - remove o item do final da lista ou do índice escolhido
del - apaga o elemento com base no índice
clear - limpa a lista
extend - estende a lista
+ - concatena listas
'''
'''lista1 = []
print(bool(lista1)) #lista vazia retorna false'''
lista = [
    123,
    True,
    "ester",
    1.2
]
print(lista)

#FATIAMENTO E ACESSO AO ITEM ESPECÍFICO
print(lista[2])

#TAMANHO DA LISTA
print(len(lista))

#EXECUTANDO MAIÚSCULO E MINÚSCULO
print(lista[2].upper(), lista[2].lower())

#TROCANDO O VALOR REFERENTE AO ÍNDICE ESPECÍFICO
lista[2] = "Hadassa"
lista[1] = False
print(lista)