# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
listaNumeros = [4, 32, 1, 34, 5, 6, 6, 21]
# lista.sort(reverse=True)
# sorted(lista) este método retorna uma nova lista ordenada. Recebe dois parâmetros: 1º a lista, 2º função(ou lambda)

print('LISTA ORDENADA COM O MÉTODO SORT')
listaNumeros.sort() #aqui ordena a lista primeiro
print(listaNumeros, end="\n\n") #para ser exibida depois

print("LISTA ORDENADA COM MÉTODO SORT DE FORMA REVERSA")
listaNumeros.sort(reverse=True)
print(listaNumeros, end="\n\n")

print('LISTA ORDENADA COM O MÉTODO SORTED')
lN = sorted(listaNumeros)
print(lN, end="\n\n")

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#Função para exibir a lista
def exibir(lista):
    for item in lista:
        print(item)
    print()

#AQUI VAMOS USAR ESSE MÉTODO DE ORDENAÇÃO, QUANDO HOUVER DICIONÁRIOS DENTRO DA LISTA
print("LISTA(COM DICIONÁRIOS) ORDENADA POR MEIO DA FUNÇÃO LAMBDA E COM SORTED")
#para ordernar uma lista com dicionário, precisa basear-se em qual chave será feita a ordenação. Neste caso a chave nome foi escolhida
l1 = sorted(lista, key=lambda item: item['nome'])
#para ordernar uma lista com dicionário, precisa basear-se em qual chave será feita a ordenação. Neste caso a chave "sobrenome" foi escolhida
l2 = sorted(lista, key=lambda item: item['sobrenome'])
exibir(l1)
exibir(l2)

print("LISTA(COM DICIONÁRIOS) ORDENADA POR MEIO DA FUNÇÃO LAMBDA E COM SORT")
lista.sort(key=lambda item:item['nome'])
exibir(lista)
