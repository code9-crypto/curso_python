from functools import partial
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p,
#         'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]


def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }


novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))


print_iter(produtos)
print(*novos_produtos, sep="\n")

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)

print()
numeros_apenas_pares = [1,2,3,4,5,6]
print(
    list(
        map(
            lambda x: x % 2 == 0,
            numeros_apenas_pares
        )
    ),
    numeros_apenas_pares,
    sep="\n"
)

numeros_apenas_impares = [1,2,3,4,5,6]
def verifica_impares(numero):
    resultado = 'impar' if numero % 2 != 0 else 'par'
    return f"{numero} -> {resultado}"

print(
    list(
        map(
            verifica_impares,
            numeros_apenas_impares
        )
    )
)