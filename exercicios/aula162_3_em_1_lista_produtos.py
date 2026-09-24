#MINHA SOLUÇÃO

#Lista de produtos
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def exibeProdutos(lista_produtos):
    for produto in lista_produtos:
        print(f"Nome: {produto['nome']}, Preco: {produto['preco']}")

#Nova lista com preço reajustado com 10% de aumento
novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)} #round -> comando para arredondar o valor e adicionar 2 casas decimais
    for produto in produtos
]

print("Lista de produtos com preço reajustado com 10% de aumento:")
exibeProdutos(novos_produtos) #como a exibição é padrão, então criei uma função para isso
print()

#Lista de produtos ordenada por nome de forma descrecente
print("Lista de produtos ordenada por nome de forma descrecente")
produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda item: item['nome'], reverse=True)
exibeProdutos(produtos_ordenados_por_nome)
print()

#Lista de produtos ordenada por preço de forma crescente
print("Lista de produtos ordenada por preço de forma crescente")
produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda prod: prod['preco'], reverse=False)
exibeProdutos(produtos_ordenados_por_preco)
print()


#SOLUÇÃO DO PROFESSOR
print("SOLUÇÃO DO PROFESSOR")
import copy

from dados import produtos

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

# FINAL

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')