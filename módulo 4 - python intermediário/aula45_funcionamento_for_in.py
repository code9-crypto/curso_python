'''
Iterável -> str, range, list etc (___iter___)
Iterador -> quem entrega um valor por vez
next -> entrega o próximo valor(um item por vez)
iter -> entrega o iterador
'''

alfabeto = "abcdefghijklmnopqrstuvwxyz" #iteravel
iterator = iter(alfabeto)#iterator

#ENTENDENDO COMO O FOR FUNCIONA USANDO O WHILE
'''while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break'''

#O FOR..IN FAZ A MESMA COISA QUE O WHILE, MAS DE FORMA BEM MAIS SIMPLES
for letra in alfabeto:
    print(letra)
