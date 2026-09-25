#MINHA SOLUÇÃO
print('MINHA SOLUÇÃO')
# lista1 = [1,2,3,4,5,6,7]
# lista2 = [1,2,3,4]

# lista1 = [4,5,6,7]
# lista2 = [10,11,12,13,14,15,16]

lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4,5,6,7,8,9,10,11]

lista_resultado = []

menor_lista = min(len(lista1), len(lista2))

def soma_listas(listaMenor, ListaMaior):

    for ind, n in enumerate(listaMenor):
        lista_resultado.insert(ind, (n + ListaMaior[ind]) )

    return lista_resultado

resultado_final = None

if len(lista1) == menor_lista:
    resultado_final = soma_listas(lista1, lista2)
else:
    resultado_final = soma_listas(lista2, lista1)

print(resultado_final, end="\n\n")



#SOLUÇÃO DO PROFESSOR
print('SOLUÇÃO DO PROFESSOR')
#esta solução é usando a função zip (baseando-se na menor lista)
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)  # Saída: [22, 4, 6, 10, 55]

#esta aqui é usando a função zip_longest (baseando-se na maior lista)
from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]