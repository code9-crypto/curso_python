# Métodos úteis dos dicionários em Python
# len - retorna quantas chaves tem
# keys - retorna nome/iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor padrão se a chave não existir
# copy - retorna uma cópia rasa (shallow copy - ele não copia uma lista para a outra variavel, mas sim aponta para a mesma lista)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}


#aqui irá mostrar a idade caso a chave exista, caso contrário será criada a chave com um valor padrão
print('idade',pessoa['idade']) if pessoa.get('idade') is not None else print('idade',pessoa.setdefault('idade', 0))

print('tamanho do dicionario por meio do método len() - conta as chaves', len(pessoa), end="\n\n")

print('conversão das chaves do dicionario para lista',list(pessoa.keys()), end="\n\n")

print('conversão dos valores do dicionario para lista',list(pessoa.values()), end="\n\n")

print('conversão da chave e valor do dicionario para lista',list(pessoa.items()), end="\n\n")

print("Exibindo as chaves por meio do dicionario")
for chave in pessoa:
    print(chave)
print()

print("Exibindo as chaves por meio do método keys()")
for chave in pessoa.keys():
    print(chave)
print()

print("Exibindo os valores do dicionário por meio do método values()")
for valor in pessoa.values():
    print(valor)
print()

print("Exibindo chave e valor por meio do método items()")
for chave, valor in pessoa.items(): #este aqui é semelhante ao método enumarete() quando há lista dentro de lista
    print(f'{chave} : {valor}')

