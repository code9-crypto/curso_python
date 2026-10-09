lista_tarefas = []
lista_desfazer = []

#Função que irá sempre exibir os itens da lista
def exibe_itens_lista():
    print("TAREFAS:")
    
    for tarefa in lista_tarefas:
        print(tarefa)

    print()
    print()


#Iniciando aplicação
while True:

    #Exibindo os comandos ao usuário E pedindo-lhe para digitar a tarefa ou comando
    print("Comandos: listar, desfazer, refazer")
    user_value = input("Digite uma tarefa ou comando: ")    
    user_value = user_value.lower().strip() #transformando o texto em minúsculo e sem espaços nas extremidades
    
    print()

    #Verificando se o valor foi um dos comandos exibidos
    match(user_value):
        case "listar":

            exibe_itens_lista()

        case "desfazer":

            if len(lista_tarefas) == 0:
                print("Nada a desfazer", end="\n\n")
                exibe_itens_lista()

            if len(lista_desfazer) == 0:
                print("Nada a desfazer", end="\n\n")
                exibe_itens_lista()

            if len(lista_tarefas) != 0:
                item_desfeito = lista_tarefas.pop()
                lista_desfazer.append(item_desfeito)
                exibe_itens_lista()

        case "refazer":
             
            if len(lista_tarefas) == 0:
                print("Nada a refazer", end="\n\n")
                exibe_itens_lista()

            if len(lista_desfazer) == 0:
                print("Nada a refazer", end="\n\n")
                exibe_itens_lista()

            if len(lista_desfazer) != 0:
                item_refeito = lista_desfazer.pop()
                lista_tarefas.append(item_refeito)
                exibe_itens_lista()

        case _: #Caso o valor não seja nenhum comando, então será adicionado na lista de tarefas
            lista_tarefas.append(user_value)
    