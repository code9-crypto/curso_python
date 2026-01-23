#DESEMPACOTAMENTO EM CHAMADAS DE MÉTODOS
string = 'ABCD'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
tupla = ('Python','é','legal')

#imprimindo os itens da um iterável um ao lado do outro
print("Imprimindo usando for..in: ", end=" ")
for item in lista:
    print(item, end=" ")
print()

#imprindo de forma mais simples
print("Fazendo direto com print: ", {*lista})

#exibindo a string e a tupla da mesma forma
print("Aqui é a variável com a string: ", *string)
print("Aqui é variavel da tuple: ", *tupla)