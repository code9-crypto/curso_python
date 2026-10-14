"""
NÃO RESOLVIDO PAREI NO MEIO DO CAMINHI
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

#LISTAS NÃO DUPLICADAS DE DOIS ITENS
#essas listas serão usadas para serem comparadas se há sequência de número duplicados. Essas são apenas 2 itens
lista1_dois_itens = set()
lista2_dois_itens = set()

#LISTAS NÃO DUPLICADAS DE TRÊS ITENS
#essas listas serão usadas para serem comparadas se há sequência de número duplicados. Essas são apenas 3 itens
lista1_tres_itens = set()
lista2_tres_itens = set()

primeiro_item_duplicado_dois_itens = None

for indice, lista in enumerate(lista_de_listas_de_inteiros): #percorrendo as listas
    
    print('Índice:',indice, 'tamanho da lista:',len(lista), ' itens:', lista)

    for x in range(0, len(lista), 2):
        
        if len(lista1_dois_itens) == 0:
            lista1_dois_itens.add(lista[x])
            lista1_dois_itens.add(lista[x+1])
        

        # for y in range(2, len(lista), 1):
        #     # if lista[y] in lista1_dois_itens:
        #     #     primeiro_item_duplicado_dois_itens = lista[y]
        #     #     lista2_dois_itens.add(lista[y])
        #     # else:
        #     #     continue
        #     if len(lista2_dois_itens) == 0:
        #         lista2_dois_itens.add(lista[y])
        #         lista2_dois_itens.add(lista[y+1])
        
            
        #     if len(lista2_dois_itens) == 2:
        #         break
            
        #     print('lista2 preenchido -> ', lista2_dois_itens)
        #     lista2_dois_itens.clear()
        
        
        print('lista1 preenchido -> ', lista1_dois_itens)
        lista2_dois_itens = lista1_dois_itens.copy()
        print('lista2 preenchido -> ', lista2_dois_itens)
        lista1_dois_itens.clear()
        
        # se o tamanho de ambos os sets forem diferentes
        # então, não houve duplicidade e ambas serão limpas para continuidade
        # if len(lista1_dois_itens) != len(lista2_dois_itens):
        #     lista1_dois_itens.clear()
        #     lista2_dois_itens.clear()
        # else:
        #     break

    print()

#SOLUÇÃO DO PROFESSOR
def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista)
    )