import decimal as dec


n1 = 0.7
n2 = 0.8
n3 = n1 + n2
print(n3)

#formatação simples de ponto flutuante com fstring
print(f"{n3:.2f}")

#comando round() faz o arrendodamento dos valores flutuantes
n1 = 5
n2 = 3
n3 = n1 / n2
print(round(n3, 4)) #1º parâmetro é o valor, 2º são as casas decimais

#usando a biblioteca decimal para também fazer a mesma coisa que round e a formatação
n1 = dec.Decimal('0.1') #o parâmetro deve ser passado em formato de string
n2 = dec.Decimal('0.7') #o parâmetro deve ser passado em formato de string
n3 = n1 / n2
print(round(n3,2))