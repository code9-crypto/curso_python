# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
print('Acessando o valor direto', p1['nome'])

print('Acessando o valor por meio do método get(caso exista)', p1.get('nome', 'Não existe'))

print('Apagando chave por meio do método pop()', p1)
nome = p1.pop('nome')
print('Não existe a chave nome', p1)


print('Apagando última chave por meio do método popitem()', p1)
ultima_chave = p1.popitem()
print('Não existe a última chave que aqui é sobrenome', p1)


#Apenas os itens(chaves) mencionados na atualização(update) serão alterados enquanto os de mais permanerão os mesmos

p1.update({
    'nome': 'novo valor',
    'idade': 30, #OBS.: caso a chave não exista, então será criada
})
print('Atualizando dicionario por meio do método update - com a escrita padrão', p1)

p1.update(nome='novo valor', idade=30)
print('Atualizando dicionario por meio do método update com parâmetros nomeados', p1)

tupla = (('nome', 'novo valor'), ('idade', 30))
p1.update(tupla)
print('Atualizando dicionario por meio de tuplas', p1)

lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print('Atualizando dicionario por meio de listas', p1)