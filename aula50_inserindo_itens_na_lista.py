lista = [10,20,30,40]
print(f"lista original: {lista}")

#INSERINDO ITEM EM QUALQUER PARTE DA LISTA COM O insert
lista.insert(0, 5)# este método usa 2 parâmetros: 1º índice, 2º valor
print(f"lista com o comando insert executado: {lista}")

#APAGANDO O ÚLTIMO ITEM DA LISTA COM O COMANDO del
#OBS.: esta forma é usada caso não saiba o tamanho correto da lista
del lista[-1]
print(f"ùltimo item deletado da lista com o comando del: {lista}")

#INSERINDO UM ITEM NO FIM DA LISTA
lista.insert(lista[-1], 50)
print(lista)

