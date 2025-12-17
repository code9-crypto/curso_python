'''
APRENDENDO A TRABALHAR COM RECORTES DE STRINGS E O MÉTODO LEN
Fatiamento [i:f:p]
i - inicio
f - fim
p - pulo
'''

nome = "Hadassa e Ester"
print(nome[5]) #assim acessamos o valor referente a este índice

print(nome[10:]) #fazendo deste jeito, ele inicia o fatiamento no índice 10 e pega todo o restante

print(nome[10:13]) #fazendo deste jeito, ele inicia o fatiamento no índice 10 e pega até o índice 13
#OBS.: o valor do último índice não é incluído

print(len(nome[10:])) #método len() devolve a quantidade de caracteres numa string

print(nome[::-1]) #esta é a forma de fazer a string ficar invertida

print(nome[len(nome)-1]) #pegando a última letra do nome
#OU
print(nome[-1])#pegando a última letra do nome