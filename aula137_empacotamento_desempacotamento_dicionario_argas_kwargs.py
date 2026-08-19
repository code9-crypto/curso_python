# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

#Extraindo os dados dos dicionários acima para criar outro dicionário completo
pessoas_completa = {**pessoa, **dados_pessoa}
print("EXTRAÇÃO DE DADOS DE DICIONÁRIOS: ", pessoas_completa, end="\n\n")

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS(tupla):', args, end="\n\n")

    print("NOMEADOS(dicionário)")
    for chave, valor in kwargs.items():
        print(chave, valor)

nao_nomeados = 1,3,5,4,6,8,4
mostro_argumentos_nomeados(*nao_nomeados, nome='Joana', qlq=123)
print()
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
outros_nao_nomeados = 'william','ester','hadassa'
mostro_argumentos_nomeados(*outros_nao_nomeados, **configuracoes)

