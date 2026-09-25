#MINHA SOLUÇÃO
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA','SP','MG','RJ']

def zipper(l1, l2):
    lista_resultado = []
    for ind, capital in enumerate(l1):
        lista_resultado.insert(ind, (capital, l2[ind]))
    return lista_resultado

print(zipper(lista1, lista2))



#SOLUÇÃO DO PROFESSOR E TAMBÉM COMO USAR AS FUNÇÕES: ZIP E ZIP_LONGEST(DO PACOTE ITERTOOLS)
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

#esta função zip(pronta do python) retorna mesmo resultado da lógica acima, mas se baseando na menor lista
print(list(zip(l1, l2))) 

#esta função zip_longest(pronta e do pacote itertools) faz mesma coisa de cima, mas agora com base na maior lista
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')), end="\n\n") #OBS.: este parâmetro "fillvalue" preenche os valores None

# função min() retorna a menor lista com base no índice
print("Função min() para encontrar a menor lista: ", min(len(l1), len(l2)))
# função max() retorna a maior lista com base no índice
print("Função max() para encontrar a maior lista: ", max(len(l1), len(l2)))