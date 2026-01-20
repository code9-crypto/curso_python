'''
Cuidados com tipos mutáveis
imutáveis = copia do valor para outra variavel
mutável = aponta para o mesmo valor na memória
'''

lista_a = [1,2,3,'c','b','a']
lista_b = lista_a.copy() #aqui a lista 'b' está recebendo uma cópia da lista 'a'
#isso significa que, quando a lista 'a' sofrer alguma alteração a lista 'b' não sofrerá esta alteração
#pois a lista 'b' e totalmente diferente da lista 'a'
