#INTERPOLAÇÃO DE STRING COM %
#s - string

#d e i - inteiro

#f - float

#x e X - hexadecimal

nome = "william"
preco = 1000.9851384
print( "%s, o preço total é R$%.2f" % (nome, preco) ) #a formatação do valor é igual a de antes com fstring
print( "o hexadecimal de %d é %04x" % (33, 33) ) #para preencher com o valor restante é possível usar deste jeito