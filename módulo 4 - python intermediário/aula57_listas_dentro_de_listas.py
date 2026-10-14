#lista de listas e seus índices

salas = [
    ['Maria','Helena'],
    ['Elaine'],
    ['Luiz','João','Eduarda']
]

#imprimindo o nome helena
print(f"Pegando o nome Helena acessando diretamente(sala[0][1]): {salas[0][1]}")
print()

#imprimindo o nome Eduarda
print(f"Pegando o nome Eduarda acessando diretamente(sala[2][2]): {salas[2][2]}")
print()

#imprimindo as salas e seus respectivos alunos com enumerate
for sala, nomes in enumerate(salas):
    print(f"Sala {sala}")
    for nome in nomes:
        print(nome, end=" ")        
    print('\n')

#OU também deste jeito
for sala, nomes in enumerate(salas):
    print(f"Sala {sala} tem esses alunos: {nomes}")