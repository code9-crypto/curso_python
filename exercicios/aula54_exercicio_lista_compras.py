#EXERCÍCIO LISTA DE COMPRAS

#imports
import os as windows

#lista de compras inicia vazia
lista_compras = []

#looping infinito que ficará perguntando ao usuário o que fazer, até ele sair
while True:    
    opcao = input("Selecione uma opção\n[i]nserir, [a]pagar, [l]istar, [s]air: ")
    print('\n')
    if opcao.lower() == 's':
        break
    elif opcao.lower() == 'i':
        windows.system('cls')
        item = input("Qual item será adicionado na lista: ")
        if item.isdigit():
            print("Número não é válido como item de compra")
        else:
            lista_compras.append(item)
    elif opcao.lower() == 'a':
        windows.system('cls')
        if len(lista_compras) == 0:
            print("Lista já está vazia")
        else:
            try:
                ind = int(input("Escolha o índice para apagar: "))
                del lista_compras[ind]
            except:
                print("Índice inválida")
    elif opcao.lower() == 'l':
        if len(lista_compras) == 0:
            print("Lista está vazia")
        else: 
            windows.system('cls')
            for idx, prod in enumerate(lista_compras):
                print(idx, prod)
    else:
        print("Opção inválida")

print("Boas compras :D")
