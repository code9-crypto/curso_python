'''
args - Argumentos não nomeados

* - *argus (empacotamento e desempacotamento)
'''

#desempacotamento
x,y,*resto = 1,2,3,4
print(x,y,resto)

#empacotamento
def soma(*args):
    #OBS.: o tipo de dado desse args é uma tupla
    total = 0
    for n in args:
        total += n
    return total

valores = 1,3,4,6,8,4,9
print(f"Total é {soma(*valores)}") #aqui está desempacotando os valores da tupla. Assim é possível passar os valores à função desta maneira