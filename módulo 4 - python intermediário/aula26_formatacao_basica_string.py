#FORMATAÇÃO BASICA DE fSTRINGS
texto = "abc"
numero = 12345.65497

#este caracter>número, irá preencher(para a esquerda) com o caracter informado até chegar a 10
print(f"{texto: >10}")

#este caracter<número, irá preencher(para a direita) com o caracter informado até chegar a 10
print(f"{texto:*<10}")

#este caracter^número, irá preencher(no centro) com o caracter informado até chegar a 10
print(f"{texto:*^10}")

#mostrando o sinal ao lado do valor(positivo ou negativo)
print(f"{numero:+.2f}")