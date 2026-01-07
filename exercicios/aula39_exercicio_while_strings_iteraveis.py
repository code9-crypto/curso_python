nome = input("Digite seu nome: ")

cont = 0

nova_string = ""
if nome != "" :
    while cont < len(nome):
        nova_string += "*"+nome[cont] #este nome[cont] é a forma de acessar individualmente a letra dentro deste iteravel
        cont += 1
    
    print(f"Seu novo nome é {nova_string}*")
else:
    print("Seu nome está vazio :(")

