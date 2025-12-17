nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
espaco = "contem" if " " in nome else "não contem"

if nome == "" or idade == "":
    print("Desculpe, você deixou campos vazios")
else:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome {espaco} espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
