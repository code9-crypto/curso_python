#VALOR PADRÃO É USADO NA DEFINIÇÃO DA FUNÇÃO
def soma(x, y, z=10):
    print(f"{x=} {y=} {z=} | x + y + z = {x + y + z}")

#chamando a função sem passar o argumento para z
soma(5, 7)

#chamando a função passando o argumento para z, o qual irá sobreescrever o valor padrão de z
soma(5, 7, 50)