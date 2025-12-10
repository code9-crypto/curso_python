# No comando print há alguns parâmetros onde são possíveis ser passados de forma nomeada
# E também é possível passar vários parâmetros não nomeados de uma vez só
#NOTA: POR PADRÃO O COMANDO print() JÁ FAZ UME QUEBRA DE LINHA AUTOMATICAMENTE

#Exemplo 1 -> passandos vários parâmetros
print(12,34,56,78,9)

#Exemplo 2 -> passando um parâmetro nomeado que fará a separação dos valores impressos
print("William","Ester","Hadassa", sep=" - ")

#Exemplo 3 -> passando um parâmetro nomeado que altera a quebra de linha
print("analista","tecnico", end=" -> ")
print("cargos")
"""observe que neste caso a palavra cargos ficará na mesma linha que a de cima, porque a quebra de linha foi alterada
pelo seta
O comando que é executado para quebra de linha é \r\n ou também pode ser \n
"""

#Exemplo 4 -> unindo tudo de uma vez
print("FAMILIA", end=" -> ")
print("Pai","Mae","Filhos", sep=" - ", end=" = ")
print("Uma familia e composta por esses membros")

