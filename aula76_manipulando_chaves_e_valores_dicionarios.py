# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# pessoa.get('sobrenome')) este método é usado para saber se uma chave existe ou não
# se a chave não existe, então por padrão seu retorno é None
# agora se ela existe, então pode-se acessar seu valor

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# FAZENDO A MESMA COISA QUE A DE CIMA SÓ QUE USANDO OPERADOR TERNÁRIO
print('NÃO EXISTE') if pessoa.get('sobrenome') is None else print(pessoa['sobrenome'])

# print('ISSO Não vai')