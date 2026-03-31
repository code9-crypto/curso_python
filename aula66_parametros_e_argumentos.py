'''
PARÂMETROS -> são as váriaveis definidas na criação da função
ARGUMENTOS -> são os valores usados no chamamento da função
 - Argumentos nomeados -> nomes usados para atrelar um valor àquele parâmetro especifico
 - Argumentos posicionais -> valores usados na mesma sequência dos parâmetros
'''

#definição
def soma(x, y, z, texto):
    print(f"{x=} {y=} {z=} | x + y + z = {x + y + z} -> {texto}")

#argumentos posicionais
soma(1 ,2 ,3, "Argumento posicional")

#argumentos nomeados
soma(x=1, y=2, z=3, texto="Argumento nomeado")

#argumentos posicionais e nomeados
soma(1, y=2, z=3, texto="Argumento posicional e nomeado")