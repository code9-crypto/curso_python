'''
args - Argumentos não nomeados

* - *argus (empacotamento e desempacotamento)
'''

#desempacotamento
x,y,*resto = 1,2,3,4
# x recebeu o número 1 (desempacotado)
# y recebeu o número 2 (desempacotado)
# *resto recebeu os outros números (empacotou o restante - 3 e 4 - em uma unica variável)
print(x,y,resto)

#empacotando os valores recebidos em uma tupla
def soma(*args): #o tipo de dado desse args é uma tupla
    total = 0
    for n in args:
        total += n
    return total

valores = 1,3,4,6,8,4,9 # isso aqui já é considerado uma tupla
print(f"Total é {soma(*valores)}") # aqui está desempacotando os valores da tupla. Assim é possível passar os valores à função desta maneira
# print(f"Total é {soma(1,3,4,6,8,4,9)}") o resultado é mesmo que o de cima