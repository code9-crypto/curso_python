'''
None = não tem valor
is e is not = tem ou não tem (tipo, valor)
NOTA: A verificação do None é feito com is ou is not

Ex.: if varivavel is None: Verificando se tem valor
        ...
    else:
        ...
    
    OU

    if variavel is not None: Verificando se não tem valor
        ...
    else:
        ...
'''

v1 = None #assim é declarado uma variável sem qualquer valor

if v1 is None:
    print("Não tem valor")
else:
    print("tem valor")

v1 = "abc"

if v1 is None:
    print("Não tem valor")
else:
    print("Tem valor")
