#ALTERANDO VALORES DA LISTA COM OS MÉTODOS: append, insert, pop, del, clear, extend, +

lista = [10, 20, 30, 40]
print(f"lista inicial: {lista}")

#REMOVENDO ITEM COM DEL
del lista[2]
print(f"lista executado o comando del: {lista}")

#ADICIONANDO ITEM NA LISTA COM O append( este adiciona ao final da lista )
lista.append(50)
print(f"lista adiciona item no final da lista: {lista}")

#REMOVENDO O ÚLTIMO ITEM DA LISTA COM O pop
valorDeletado = lista.pop() #OBS.: este remove o item da lista e também retorna o item deletado
print(f"lista com o último elemento removido: {lista},\n o valor apagado foi: {valorDeletado}")