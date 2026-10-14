'''
for..in + range
range -> range(start, end, step)
OBS.: o range também é um iterável. O valor que será o end não entra na contagem
'''

numeros = range(0, 10, 1)
for num in numeros:
    print(num)